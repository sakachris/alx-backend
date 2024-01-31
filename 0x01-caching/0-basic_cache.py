#!/usr/bin/env python3
''' 0-basic_cache.py '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    inherits from BaseCaching and is a caching system
    '''

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data the item value for the key key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        return the value in self.cache_data linked to key or none
        '''
        if key is not None:
            return self.cache_data.get(key)
