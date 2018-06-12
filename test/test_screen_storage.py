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
        screen_storage.create("Print to screen")
        self.assertEqual(mock_stdout.getvalue(), text)

    def test_remove(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.remove, 1)

    def test_update(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.update, 1)

    def test_read(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.read, 1)

    def test_read_all(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.read_all)

    def test_remove_all(self):
        screen_storage = ScreenStorage()
        self.assertRaises(UnsupportedOperationError, screen_storage.remove_all)
