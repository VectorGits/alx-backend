#!/usr/bin/env python3
"""
Least Recent Used cache replacement algorithm
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Put Item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """Get an Item by key"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
