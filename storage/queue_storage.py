from abc import abstractmethod


class CollectorQueueStorage:

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def consume(self):
        pass
