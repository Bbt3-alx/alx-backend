#!/usr/bin/env python3
"""Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""

    def put(self, key, item):
        """Add an item in the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
