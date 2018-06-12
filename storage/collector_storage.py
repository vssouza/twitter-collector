from abc import ABCMeta, abstractmethod


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
    def read(self, data):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def remove_all(self):
        pass
