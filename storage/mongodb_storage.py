from storage.collector_storage import CollectorStore
from pymongo import MongoClient
from exception import UnsupportedOperationError


class MongoDBStorage(CollectorStore):

    def __init__(self, host_address, port, username, password, database):
        self.host_address = host_address
        self.port = port
        url = 'mongodb://{0}:{1}@{2}:{3}'.format(username, password, host_address, port)
        self.client = MongoClient(url)
        self.database = self.client.get_database(database)

    def write(self, data):
        collection = self.database[data['collection']]
        return collection.insert_one(data['json']).inserted_id

    def remove(self, data):
        raise UnsupportedOperationError()

    def update(self, data):
        raise UnsupportedOperationError()

    def read_by_id(self, data):
        collection = self.database[data['collection']]
        return collection.find_one({"_id": data['object_id']})

    def read_all(self):
        raise UnsupportedOperationError()

    def remove_all(self):
        raise UnsupportedOperationError()

    def read_by_attribute(self, attribute, value):
        raise UnsupportedOperationError()

    def read_by_attributes(self, data):
        raise UnsupportedOperationError()

    def close(self):
        self.client.close()
