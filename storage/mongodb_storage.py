from storage.db_storage import CollectorDBStorage
from pymongo import MongoClient
from exception import InvalidParameterError


class MongoDBStorage(CollectorDBStorage):

    def __init__(self, url, database):
        self._client = MongoClient(url)
        self._database = self._client.get_database(database)

    def write(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.insert_one(data['json']).inserted_id

    def update_by_id(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.update_one({'_id': data['object_id']}, {"$set": data['json']}, upsert=False)

    def update_by_attributes(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.update_many(data['attributes'], {"$set": data['json']}, upsert=False)

    def read_by_id(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.find_one({'_id': data['object_id']})

    def read_all(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.find({})

    def read_by_attributes(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.find(data['attributes'])

    def remove_by_id(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.delete_one({'_id': data['object_id']}).deleted_count

    def remove_all(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.delete_many({}).deleted_count

    def remove_by_attributes(self, data):
        self.validate_collection(data)
        collection = self._database[data['collection']]
        return collection.delete_many(data['attributes']).deleted_count

    def drop_database(self):
        self._client.drop_database(self._database)

    def drop_collection(self, data):
        self.validate_collection(data)
        self._database.drop_collection(data['collection'])

    def close(self):
        self._client.close()

    @staticmethod
    def validate_collection(data):
        if 'collection' not in data.keys():
            raise InvalidParameterError('collection')

    @staticmethod
    def get_mongodb_url(hostname, port, username, password):
        return "mongodb://{0}:{1}@{2}:{3}/".format(username, password, hostname, port)
