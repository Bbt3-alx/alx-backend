#!/usr/bin/env python3
"""Least Recently Caching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used (LRU) Caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item from cache by it's key"""
        if key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
