from django.core.cache import cache

from src.hydra_cache.utils.hasher import md5


def flush_cache_for_keys(_keys, pre_hash=None):
    """
        Flushes the cache for the given keys.

        Args:
            _keys (str or list): The key(s) to flush the cache for.
            pre_hash (str, optional): A pre-hash to use for the keys. Defaults to None.

        Returns:
            None
        """
    post_hash = None
    if pre_hash is not None:
        ctx = md5(usedforsecurity=False)
        ctx.update(pre_hash.encode())
        post_hash = ctx.hexdigest()

    """
    Flush the cache for the given key.
    """
    if type(_keys) == str:
        _keys = [_keys]
    for key in _keys:
        keys = cache._cache.get_client().keys(f"*{key}*{post_hash}*" if post_hash else f"*{key}*")
        if len(keys) > 0:
            print(f"Flushing cache for {keys}")
            cache._cache.get_client().delete(
                *keys
            )
