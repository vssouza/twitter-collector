from storage.collector_storage import CollectorStore
from exception import UnsupportedOperationError


class ScreenStorage(CollectorStore):

    def write(self, data):
        print(data)

    def remove(self, data):
        raise UnsupportedOperationError()

    def update(self, data):
        raise UnsupportedOperationError()

    def read(self, data):
        raise UnsupportedOperationError()

    def read_all(self):
        raise UnsupportedOperationError()

    def remove_all(self):
        raise UnsupportedOperationError()

    def read_by_attribute(self, attribute, value):
        raise UnsupportedOperationError()

    def read_by_attributes(self, data):
        raise UnsupportedOperationError()

