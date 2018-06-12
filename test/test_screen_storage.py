from io import StringIO
from unittest import TestCase
from storage import ScreenStorage
from exception import UnsupportedOperationError
import unittest.mock


class TestScreenStorage(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        text = "Print to screen\n"
        screen_storage = ScreenStorage()
        screen_storage.write("Print to screen")
        self.assertEqual(mock_stdout.getvalue(), text)

    def test_remove(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.remove, 1)

    def test_update(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.update, 1)

    def test_read_by_id(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.read_by_id, 'attribute')

    def test_read_by_attribute(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.read_by_attribute, 'attribute', 'value')

    def test_read_by_attributes(self):
        screen_storage = ScreenStorage()
        attributes = {
            'attribute_1': 'value',
            'attribute_2': 'value_b',
        }
        self.assertRaises(UnsupportedOperationError, screen_storage.read_by_attributes, attributes)

    def test_read_all(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.read_all)

    def test_remove_all(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.remove_all)
