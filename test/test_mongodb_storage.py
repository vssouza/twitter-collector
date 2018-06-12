from unittest import TestCase
from storage import MongoDBStorage


class TestMongoDBStorage(TestCase):

    hostname = "localhost"
    port = 27017
    username = "admin"
    password = "admin"
    database = "test_db"

    def test_write(self):
        mongodb_collector = MongoDBStorage(self.hostname, self.port, self.username, self.password, self.database)
        test_json = {"test": "data"}
        data = {"collection": "test_collection", "json": test_json}
        data["object_id"] = mongodb_collector.write(data)
        retrieved_json = mongodb_collector.read_by_id(data)
        mongodb_collector.close()
        self.assertEqual(test_json["test"], retrieved_json["test"])
