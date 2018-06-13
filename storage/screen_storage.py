from storage.collector_storage import CollectorStore
from exception import UnsupportedOperationError


class ScreenStorage(CollectorStore):

    def write(self, data):
        print(data)

    def remove_by_id(self, data):
        raise UnsupportedOperationError()

    def remove_by_attributes(self, data):
        raise UnsupportedOperationError()

    def update(self, data):
        raise UnsupportedOperationError()

    def read_by_id(self, data):
        raise UnsupportedOperationError()

    def read_all(self, data):
        raise UnsupportedOperationError()

    def remove_all(self, data):
        raise UnsupportedOperationError()

    def read_by_attributes(self, data):
        raise UnsupportedOperationError()

    def close(self):
        raise UnsupportedOperationError()
