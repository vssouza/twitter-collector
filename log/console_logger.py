import logging
from log.log_util import LogUtil


class ConsoleLogger:

    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR

    def __init__(self, class_name, handler_level):
        self._logger = logging.getLogger(class_name)
        ch = logging.StreamHandler()
        self._logger.setLevel(handler_level)
        ch.setFormatter(logging.Formatter(LogUtil.log_format))
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
