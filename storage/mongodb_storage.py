from storage.collector_storage import CollectorStore


class MongoDBStorage(CollectorStore):

    def __init__(self, collection):
        self.collection = collection
