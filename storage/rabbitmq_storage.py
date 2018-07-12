from storage.queue_storage import CollectorQueueStorage


class RabbitMQStorage(CollectorQueueStorage):
    def __init__(self):
        print("TODO: create rabbitmq class")

    def post(self):
        print("TODO post message to queue")

    def consume(self):
        print("TODO consume message from queue")
