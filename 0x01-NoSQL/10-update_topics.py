#!/usr/bin/env python3
'''Task 10 module'''


def update_topics(mongo_collection, name, topics):
    '''update topics based on name'''
    data = mongo_collection.update_many({name: name}, {$set: {topics: topics}})
