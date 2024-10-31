# /usr/bin/env python3
"""Least Frequently used caching"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """The least Frequently Used Caching System"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequence = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequence.values())
            lfu_key = min(
                (k for k in self.frequence if self.frequence[k] == min_freq),
                key=lambda k: self.frequence[k],
            )

            del self.cache_data[lfu_key]
            del self.frequence[lfu_key]
            print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item
        self.frequence[key] = self.frequence.get(key, 0) + 1

    def get(self, key):
        """Get a cache by ket"""
        if not key or key not in self.cache_data:
            return None

        self.frequence[key] += 1
        return self.cache_data[key]
