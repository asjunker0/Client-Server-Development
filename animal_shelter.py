#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:29:48 2025

@author: abbigalejunke_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, host, port, db, col):
        self.HOST = host
        self.PORT = port
        self.DB = db
        self.COL = col

        self.client = MongoClient(f'mongodb://{self.HOST}:{self.PORT}')
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, query):
        if isinstance(query, dict):
            results = list(self.collection.find(query))
            return results
        else:
            return[]
        
# Method to implement the U in CRUD
    def update(self, query, updated_value):
        if query and updated_value and isinstance(query, dict) and isinstance(updated_value, dict):
            result = self.collection.update_many(query, {"$set": updated_value})
            return result.modified_count > 0
        else:
            return Exception("Unable to update data")
        
# Method to implement D in CRUD
    def delete(self, query):
        if query and isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count > 0
        else:
            raise Exception("Invalid query for deletion")
        