#!/usr/bin/env python3
'''Task 9 module'''


def insert_school(mongo_collection, **kwargs):
    '''insert new doc in collection'''
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
