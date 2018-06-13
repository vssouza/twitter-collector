from abc import abstractmethod


class CollectorStore:

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def remove_by_id(self, data):
        pass

    @abstractmethod
    def remove_by_attributes(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def read_by_id(self, data):
        pass

    @abstractmethod
    def read_by_attributes(self, data):
        pass

    @abstractmethod
    def read_all(self, data):
        pass

    @abstractmethod
    def remove_all(self, data):
        pass

    @abstractmethod
    def close(self):
        pass
