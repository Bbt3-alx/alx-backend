#!/usr/bin/env python3
"""The Most Recently Used Caching"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """The Most Recently Used Cashing system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop()
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get a cache by key"""
        if not key or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
