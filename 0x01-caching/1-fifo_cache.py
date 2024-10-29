#!/usr/bin/env python3
"""FIFO caching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class of FIFO caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if not key or not item:
            return

        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            discared = next(iter(self.cache_data))
            self.cache_data.pop(discared)
            print(f"DISCARD: {discared}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
