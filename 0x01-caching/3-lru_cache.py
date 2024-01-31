#!/usr/bin/env python3
''' 3-lru_cache.py '''

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data the item value for the key key
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discarding least recently used item
                lru_key = self.order_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            # Adding new item
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        '''
        return the value in self.cache_data linked to key
        '''
        if key is not None and key in self.cache_data:
            # updating order list when item accessed
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        else:
            return None
