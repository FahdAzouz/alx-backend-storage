#!/usr/bin/env python3
'''Task 11 module'''


def schools_by_topic(mongo_collection, topic):
    '''return list schools with specific topic'''
    return mongo_collection.find({'topics': {'$in': [topic]}})
