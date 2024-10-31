#!/usr/bin/env python3
"""LIFO Caching"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A simple LIFO caching system"""

    def __init__(self):
        """Class initialization"""
        super().__init__()

    def put(self, key, item):
        """add an item in the cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discared = self.cache_data.popitem()
            print(f"DISCARD: {discared[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """Get a cache by its key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
