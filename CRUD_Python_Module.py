# Example Python Code to Insert a Document 
# username zgarrett

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER,PASS,HOST,PORT)
        ) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: 
                self.collection.insert_one(data)  # data should be dictionary
                return True
            else: 
                return False
        except Exception as e:
            print ("Error inserting documents:", e)
            return False
            
    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None:
                results = self.collection.find(query)
                return list(results)
            else:
                return []
        except Exception as e:
            print("Error reading documents:", e)
            return []
        
    # Update matching documents in the database
    def update(self, query, new_values):
        try:
            if query is not None and new_values is not None:
                result = self.collection.update_many(
                    query, {"$set": new_values}
                )
                return result.modified_count
            else:
                return 0

        except Exception as e:
            print("Error updating documents:", e)
            return 0
        
    # Delete matching documents from the database
    def delete(self, query):
        try:
            if query is not None:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0

        except Exception as e:
            print("Error deleting documents:", e)
            return 0