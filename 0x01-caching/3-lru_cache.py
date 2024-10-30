#!/usr/bin/env python3
"""LRU Csching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used (LRU) Caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Add an item to cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            discarded = self.cache_data.pop(first_key)
            print(f"DISCARD: {discarded[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by it's key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
