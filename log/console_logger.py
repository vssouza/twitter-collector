import logging
from log.base_logger import BaseLogger


class ConsoleLogger(BaseLogger):

    def __init__(self, class_name, handler_level):
        self._logger = logging.getLogger(class_name)
        ch = logging.StreamHandler()
        self._logger.setLevel(handler_level)
        ch.setFormatter(logging.Formatter(BaseLogger.LOG_FORMAT, datefmt=BaseLogger.DATE_FORMAT))
        self._logger.addHandler(ch)

    def info(self, message):
        self._logger.info(message)

    def debug(self, message):
        self._logger.debug(message)

    def warning(self, message):
        self._logger.warning(message)

    def critical(self, message):
        self._logger.critical(message)

    def error(self, message):
        self._logger.error(message)

    def exception(self, message, exception):
        self._logger.exception(message, exception)
