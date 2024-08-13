#!/usr/bin/env python3
"""
Python funct that lists all docs in a collection:
    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
"""
import pymongo


def list_all(mongo_collection):
    """Return list of all documents"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
