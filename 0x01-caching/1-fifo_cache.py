#!/usr/bin/env python3
''' 1-fifo_cache.py '''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data the item value for the key
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discarding first item if cache is full
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Adding new item
            self.cache_data[key] = item

    def get(self, key):
        '''
        return the value in self.cache_data linked to key
        '''
        if key is not None:
            return self.cache_data.get(key)
