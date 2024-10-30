#!/usr/bin/env python3
"""
Most Recently Used cache replacement algorithm
"""


from base_caching import BaseCaching


class MRUCaching(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru.remove(key)
        self.cache_data[key] = item
        self.mru.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.mru.pop(-2)
            print("DISCARD: {}".format(last))
            del self.cache_data[last]

    def get(self, key):
        """Get an Item by key"""
        if key is None or key not in self.cache_data:
            self.mru.remove(key)
            self.mru.append(key)
        return self.cache_data.get(key, None)
