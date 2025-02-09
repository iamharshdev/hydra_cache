from django.conf import settings
from django.core.cache import cache
from django.utils.cache import get_cache_key
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from hydra_cache.utils.cache import flush_cache_for_keys


class HydraCacheMixin:
    """
   A mixin that provides cache control functionality for Django views.
   """
    cache_key_prefix = None  # The prefix for the cache key
    disable_cache = False  # Flag to disable caching for the view
    cache_timeout = settings.CACHE_TIMEOUT  # Cache timeout in seconds
    vary_on_header = 'X-CustomHeader'  # HTTP header to vary the cache on
    match_on_cache_key = False  # Whether to use the generated cache key for cache clearing
    clear_cache_keys = []  # List of cache keys to clear on POST, PUT, DELETE, PATCH
    cache_hash_header = True  # Whether to use the header value in the cache key hash

    def get_cache_key(self, request):
        """
        Return the cache key for the request.
        """
        return get_cache_key(request, self.cache_key_prefix, "GET", cache=cache)

    @classmethod
    def as_view(cls, **initkwargs):
        """
       Wrap the view with cache_page decorator and vary_on_headers if needed.
       """
        view = super().as_view(**initkwargs)
        if cls.disable_cache:
            return view
        view = vary_on_headers(cls.vary_on_header)(view) if cls.vary_on_header else view
        return cache_page(cls.cache_timeout, key_prefix=cls.cache_key_prefix)(view)

    def clear_cache(self, request):
        """
       Clear the cache for the current request.
       """

        cache_keys = self.clear_cache_keys if len(self.clear_cache_keys) > 0 else [self.cache_key_prefix]
        cache_keys = cache_keys if self.match_on_cache_key else [self.get_cache_key(request)]
        flush_cache_for_keys(cache_keys, request.META.get(f'HTTP_{self.vary_on_header.replace("-", "_").upper()}', '') if self.cache_hash_header else None)

    def dispatch(self, request, *args, **kwargs):
        """
       Dispatch the request and clear the cache if necessary.
       """
        response = super().dispatch(request, *args, **kwargs)
        if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            self.clear_cache(request)
        return response
