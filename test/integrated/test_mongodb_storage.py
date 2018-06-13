from unittest import TestCase
from storage import MongoDBStorage
from bson import ObjectId


class TestMongoDBStorage(TestCase):

    hostname = "localhost"
    username = "admin"
    password = "admin"
    database = "test_db"

    def setUp(self):
        url = MongoDBStorage.get_mongodb_url('localhost', 27017, 'admin', 'admin')
        self.mongodb_collector = MongoDBStorage(url, 'collector_test_db')

    def setup_db_initial_data(self):
        test_json = {'_id': ObjectId('53fbf4615c3b9f41c381b6a3'), 'name': 'john', 'lastname': 'constantine'}
        data = {'collection': 'test_collection', 'json': test_json}
        self.mongodb_collector.write(data)
        test_json = {'_id': ObjectId('53fbf4615c3b9f41c381b6a4'), 'name': 'natasha', 'lastname': 'romanov'}
        data = {'collection': 'test_collection', 'json': test_json}
        self.mongodb_collector.write(data)
        test_json = {'_id': ObjectId('53fbf4615c3b9f41c381b6a5'), 'name': 'steve', 'lastname': 'rogers'}
        data = {'collection': 'test_collection', 'json': test_json}
        self.mongodb_collector.write(data)
        test_json = {'_id': ObjectId('53fbf4615c3b9f41c381b6a6'), 'name': 'steve', 'lastname': 'trevor'}
        data = {'collection': 'test_collection', 'json': test_json}
        self.mongodb_collector.write(data)

    def tearDown(self):
        data = {'collection': 'test_collection'}
        self.mongodb_collector.remove_all(data)
        self.mongodb_collector.drop_database()
        self.mongodb_collector.close()

    def test_write(self):
        test_json = {'_id': ObjectId('53fbf4615c3b9f41c381b6a3'), 'name': 'steve', 'lastname': 'trevor'}
        data = {'collection': 'test_collection', 'json': test_json}
        result = self.mongodb_collector.write(data)
        self.assertEqual(test_json["_id"], result)
        self.assertEqual(test_json["name"], "steve")

    def test_read_by_id(self):
        self.setup_db_initial_data()
        data = {'collection': 'test_collection', 'object_id': ObjectId('53fbf4615c3b9f41c381b6a3')}
        result = self.mongodb_collector.read_by_id(data)
        self.assertEqual(result['name'], "john")

    def test_read_by_attributes(self):
        self.setup_db_initial_data()
        attributes = {'name': 'steve'}
        data = {'collection': 'test_collection', 'attributes': attributes}
        result = self.mongodb_collector.read_by_attributes(data)
        list_result = list(result)
        self.assertEqual(2, len(list_result))
        self.assertEqual(list_result[0]['lastname'], 'rogers')
        self.assertEqual(list_result[1]['lastname'], 'trevor')

    def test_read_all(self):
        self.setup_db_initial_data()
        data = {'collection': 'test_collection'}
        result = self.mongodb_collector.read_all(data)
        list_result = list(result)
        self.assertEqual(len(list_result), 4)
        self.assertEqual(list_result[0]['name'], "john")
        self.assertEqual(list_result[1]['name'], "natasha")
        self.assertEqual(list_result[2]['name'], "steve")

    def test_remove_by_id(self):
        self.setup_db_initial_data()
        data = {'collection': 'test_collection', 'object_id': ObjectId('53fbf4615c3b9f41c381b6a3')}
        result = self.mongodb_collector.remove_by_id(data)
        self.assertEqual(result, 1)

    def test_remove_by_attributes(self):
        self.setup_db_initial_data()
        attributes = {'name': 'steve'}
        data = {'collection': 'test_collection', 'attributes': attributes}
        result = self.mongodb_collector.remove_by_attributes(data)
        self.assertEqual(result, 2)

    def test_remove_all(self):
        self.setup_db_initial_data()
        data = {'collection': 'test_collection'}
        result = self.mongodb_collector.remove_all(data)
        self.assertEqual(result, 4)

    def test_update_by_id(self):
        self.setup_db_initial_data()
        test_json = {'name': 'james', 'lastname': 'howlet'}
        data = {'collection': 'test_collection', 'object_id': ObjectId('53fbf4615c3b9f41c381b6a6'), 'json': test_json}
        result = self.mongodb_collector.update_by_id(data)
        self.assertEqual(result.matched_count, 1)
        data = {'collection': 'test_collection', 'object_id': ObjectId('53fbf4615c3b9f41c381b6a6')}
        result = self.mongodb_collector.read_by_id(data)
        self.assertEqual(result['name'], "james")
        self.assertEqual(result['lastname'], "howlet")

    def test_update_by_attribute(self):
        self.setup_db_initial_data()
        test_json = {'situation': 'dismissed'}
        attributes = {'name': 'steve'}
        data = {'collection': 'test_collection', 'attributes': attributes, 'json': test_json}
        result = self.mongodb_collector.update_by_attributes(data)
        self.assertEqual(result.matched_count, 2)
        attributes = {'situation': 'dismissed'}
        data = {'collection': 'test_collection', 'attributes': attributes}
        result = self.mongodb_collector.read_by_attributes(data)
        list_result = list(result)
        self.assertEqual(len(list_result), 2)
        self.assertEqual(list_result[0]['lastname'], 'rogers')
        self.assertEqual(list_result[1]['lastname'], 'trevor')
