from abc import abstractmethod


class CollectorDBStorage:

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
    def update_by_id(self, data):
        pass

    @abstractmethod
    def update_by_attributes(self, data):
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
