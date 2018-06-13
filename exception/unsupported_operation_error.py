
class UnsupportedOperationError(Exception):
    def __init__(self):
        self.message = "Operation not supported."
        super().__init__(self.message)
