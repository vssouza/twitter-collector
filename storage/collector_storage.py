from abc import abstractmethod


class CollectorStore:

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def remove(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def read_by_id(self, data):
        pass

    @abstractmethod
    def read_by_attribute(self, attribute, value):
        pass

    @abstractmethod
    def read_by_attributes(self, data):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def remove_all(self):
        pass

    @abstractmethod
    def close(self):
        pass
