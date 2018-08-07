from abc import abstractmethod


class CollectorQueueStorage:

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def consume(self):
        pass

    @abstractmethod
    def create_partition(self):
        pass
