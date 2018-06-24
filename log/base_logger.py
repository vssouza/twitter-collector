import logging
from abc import abstractmethod


class BaseLogger:

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def critical(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def exception(self, message, exception):
        pass