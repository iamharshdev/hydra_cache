# Hydra Cache: The Ultimate Solution for Taming the Caching Chaos

![image](https://github.com/iamharshdev/hydra_cache/assets/46974223/5ca1e942-13e6-4e6e-90c7-3823adc5ed7f)


Yo, what's up my fellow Django devs? You know what really grinds my gears? Dealing with caching in web apps. It's like trying to catch a greased-up, naked guy in a pool of Vaseline. But fear not, my dudes, because Hydra Cache is here to save the day (and your sanity).

## The Legend

In the depths of web development lore, there lurks a terrifying creature known as the Kraken of Caching Complexity. This multi-headed monstrosity has been ensnaring developers in its tangled tentacles, leaving them adrift in a sea of stale data and suboptimal performance. But fear not, my brave memers oh devs sorry!, for Hydra Cache is here to slay this beast once and for all!

## Why I Built Hydra Cache

Look, I've been there, okay? I've spent countless nights battling this caching nightmare, writing the same boilerplate code over and over again, like some kind of masochistic ritual. But no more, my fellas! I created Hydra Cache to save you from this madness, so you can spend more time scrolling through lusty memes! Oops, ~just memes~

With Hydra Cache, you can:

- **Reduce Boilerplate Code**: No more copy-pasting the same caching logic across your views. Just inherit from `HydraCacheMixin`, and you're good to go, bruh!
- **Centralize Caching Configuration**: Kiss goodbye to the days of hunting down caching configurations scattered across your codebase. With Hydra Cache, you control it all from one central location, like a true meme lord.
- **Consistent Caching Patterns**: Consistency is key, my dudes. Hydra Cache ensures that your caching logic follows a standardized approach, making it easier for your team (and your future self) to understand and maintain, even after a night of binge-watching memes.
- **Flexible Cache Invalidation**: Stale data? Not on my watch! Hydra Cache automatically invalidates your cache after `POST`, `PUT`, `DELETE`, and `PATCH` requests, keeping your app fresher than a meme.
- **Fine-Grained Cache Clearing**: With the `match_on_cache_key` option, you can clear the cache with surgical precision, targeting specific keys and leaving the rest untouched. No more scorched-earth cache purging!
- **Easy Integration**: Hydra Cache plays nice with Django's built-in caching system, so you can leverage your existing cache backends without any extra hassle, just like how porn clips seamlessly integrate into your daily life! Not your ex!.

## Key Features

- **Cache Key Sorcery**: Weave intricate cache keys, summoning the power of timeouts and vary headers like a true caching wizard, but with the dankness of a meme lord.
- **Automatic Cache Purging**: Unleash the fury of automatic cache invalidation, cleansing your app of stale data with the force of a raging maelstrom, or a dank meme going viral.
- **Fine-Grained Cache Clearing**: Clear the cache with surgical precision, slicing through cache keys like a skilled samurai, or like a dank meme slicing through the internet.
- **Seamless Integration**: Harness the power of Django's caching system without breaking a sweat, just like how you effortlessly integrate memes into your conversations.
- **Extensible Might**: Customize and extend Hydra Cache to fit your twisted caching desires, like a mad scientist tinkering with an unholy creation, or a meme lord crafting the dankest memes.

## Getting Started

Alright, listen up, my fellow memers! Here's how you summon the Kraken of Caching Awesomeness:

1. Install the package like a true caching warrior: `pip install boring-hydra-cache`
2. In your Django views, import the `HydraCacheMixin` like you're summoning an ancient caching ritual: `from hydra_cache.mixins import HydraCacheMixin`
3. Create a view class that inherits from both `HydraCacheMixin` and your desired Django view class, binding the Kraken to your unholy will:

```python
from django.views.generic import APIView
from hydra_cache.mixins import HydraCacheMixin

class MyListView(HydraCacheMixin, APIView):
    cache_key_prefix = 'my_list_view'
    cache_timeout = 3600  # 1 hour
    vary_on_header = 'X-Requested-With'

```

1. In a scenario where you have two separate views - `MyListView` for listing data and `MyCreateUpdateView` for creating or updating data, you can use Hydra Cache to ensure that the cache for `MyListView` is cleared whenever new data is created, updated, or deleted.

First, ensure that both views inherit from `HydraCacheMixin`

In `MyCreateUpdateView`, you would set the `match_on_cache_key` attribute to `True` and list `my_list_view` in the `clear_cache_keys` attribute:

```python
class MyCreateUpdateView(HydraCacheMixin, APIView):
    ...
    match_on_cache_key = True
    clear_cache_keys = ['my_list_view']
    disable_cache = True
```

With this setup, any `POST`, `PUT`, `DELETE`, or `PATCH` request made through `MyCreateUpdateView` will automatically clear the cache for `MyListView`, ensuring that the list view always displays the most recent data.

And just like that, my friends, you've harnessed the power of Hydra Cache, commanding the multi-headed Kraken of Caching Awesomeness and charting a course towards unparalleled performance and scalability!

But wait, there's more! With Hydra Cache, you have the power to unleash the Kraken's fury upon your cache whenever you desire, like a true sucker. While the `HydraCacheMixin` automatically handles cache invalidation for `POST`, `PUT`, `DELETE`, and `PATCH` requests, you can also clear the cache independently within your model signals, custom commands, or any other part of your application.

Behold the mighty `flush_cache_for_keys` method, a potent incantation that summons the Kraken's wrath upon specific cache keys:

```python
from hydra_cache.utils import flush_cache_for_keys
```

For example, within a Django model signal, you could clear the cache for a specific object:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from hydra_cache.utils import flush_cache_for_keys

@receiver(post_save, sender=MyModel)
def clear_my_model_cache(sender, instance, **kwargs):
    cache_key_prefix = f'my_model_{instance.pk}'
    flush_cache_for_keys(cache_key_prefix)

```

## Conclusion

Look, I get it. Caching can be a real pain in the neck, but with Hydra Cache, you can finally tame the beast and take control of your caching strategies. No more boilerplate code, no more scattered configurations, and no more stale data nightmares. Just pure, unadulterated caching awesomeness!

So what are you waiting for? Embrace the Kraken, and let the tides of caching ever be in your favor, my fellow meme lords!
