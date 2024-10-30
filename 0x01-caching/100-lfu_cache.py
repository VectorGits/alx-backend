#!/usr/bin/env python3
"""
Least Frequently Used cache replacement algorithm
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []
        self.frequency = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        self.cache_data[key] = item
        self.keys.append(key)

        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
            if len(lfu_keys) > 1:
                lfu_key = next(k for k in self.keys if k in lfu_keys)
            else:
                lfu_key = lfu_keys[0]

            self.keys.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            print("DISCARD: {}".format(lfu_key))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data.get(key)
