#!/usr/bin/env python3
'''Module 0
'''

import redis
from uuid import uuid4
from typing import Union


class Cache:
    '''declares a cash redis class'''
    def __init__(self):
        '''upon init bla bla'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> string:
        '''generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.'''
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey
