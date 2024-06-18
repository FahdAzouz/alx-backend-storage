#!/usr/bin/env python3
'''Task 8 module'''


def list_all(mongo_collection):
    '''list all docs in collection'''
    list = mongo_collection.find()
    return list
