from storage.db_storage import CollectorStore
from pymongo import MongoClient


class MongoDBStorage(CollectorStore):

    def __init__(self, url, database):
        self.client = MongoClient(url)
        self.database = self.client.get_database(database)

    def write(self, data):
        collection = self.database[data['collection']]
        return collection.insert_one(data['json']).inserted_id

    def update_by_id(self, data):
        collection = self.database[data['collection']]
        return collection.update_one({'_id': data['object_id']}, {"$set": data['json']}, upsert=False)

    def update_by_attributes(self, data):
        collection = self.database[data['collection']]
        return collection.update_many(data['attributes'], {"$set": data['json']}, upsert=False)

    def read_by_id(self, data):
        collection = self.database[data['collection']]
        return collection.find_one({'_id': data['object_id']})

    def read_all(self, data):
        collection = self.database[data['collection']]
        return collection.find({})

    def read_by_attributes(self, data):
        collection = self.database[data['collection']]
        return collection.find(data['attributes'])

    def remove_by_id(self, data):
        collection = self.database[data['collection']]
        return collection.delete_one({'_id': data['object_id']}).deleted_count

    def remove_all(self, data):
        collection = self.database[data['collection']]
        return collection.delete_many({}).deleted_count

    def remove_by_attributes(self, data):
        collection = self.database[data['collection']]
        return collection.delete_many(data['attributes']).deleted_count

    def drop_database(self):
        self.client.drop_database(self.database)

    def drop_collection(self, data):
        self.database.drop_collection(data['collection'])

    def close(self):
        self.client.close()

    @staticmethod
    def get_mongodb_url(hostname, port, username, password):
        return "mongodb://{0}:{1}@{2}:{3}/".format(username, password, hostname, port)
