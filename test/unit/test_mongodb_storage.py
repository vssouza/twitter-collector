from unittest import TestCase
from storage import MongoDBStorage
from mockupdb import go, MockupDB


class TestMongoDBStorage(TestCase):

    hostname = "localhost"
    username = "admin"
    password = "admin"
    database = "test_db"

    def test_write(self):
        test_json = {'_id': '123ab-456cd-789ef', 'test': 'data'}
        data = {'collection': 'test_collection', 'json': test_json}
        mongodb_collector = self.server_setup()
        future = go(mongodb_collector.write, data)
        result = self.server_proceed(future)
        self.assertEqual(test_json["_id"], result)
        self.server_shutdown()

    def server_setup(self):
        self.server = MockupDB(auto_ismaster={"maxWireVersion": 3})
        self.server.run()
        return MongoDBStorage(self.server.uri, self.database)

    def server_proceed(self, future):
        cmd = self.server.receives()
        cmd.ok()
        return future()

    def server_shutdown(self):
        self.server.stop()
