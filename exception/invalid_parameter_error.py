
class InvalidParameterError(Exception):
    def __init__(self, parameter):
        self.message = "The parameter provided for {0} is invalid.".format(parameter)
        super().__init__(self.message)
