'''
Logging module. A class has been designed just in case different instances are required
(to be called from different modules).
'''

import logging              # Basic import.
from inspect import stack   # Needed so as to retrieve function caller's name.

from unittest.mock import patch, MagicMock
import pytest

class DataLogger:
    """
    Provides a logging utility for a Python module.

    This class initializes a logger instance for a module and sets its
    logging level to DEBUG by default. It can be used to log messages
    throughout the module consistently.

    Attributes:
        _logger : logging.Logger
            Instance of a Python logger used for recording debug and info messages.
    """
    
    __log_format    : str               = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
    __logger        : logging.Logger    = None
    __log_caller_fn : bool              = None

    def __init__(self, name: str = __name__, level: int = logging.DEBUG, log_caller_fn: bool = True):
        """
            Initializer logger object (constructor method).
            
            Args:
                name            : Logger's target name.
                level           : Logger's level (the closer to DEBUG / lower, the more detailed the output will be).
                log_caller_fn   : Tells whether the calling function's name should be logged.
        """
                
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(level)
        self.__logger.propagate = False # Just in case.

        if not self.__logger.handlers:  # Only add a handler if none exists
            self.handler = logging.StreamHandler()
            self.handler.setFormatter(logging.Formatter(self.__log_format))
            self.__logger.addHandler(self.handler)

        self.__log_caller_fn = log_caller_fn


    def _addCallerFunctionsName(self, msg: str) -> str:
        """
            Adds caller function's name (if required).
            
            Args:
                msg : Message to be logged.
            
            Returns:
                Processed message.
        """
        return ('(' + stack()[2].function + ") " + msg) if self.__log_caller_fn else msg


    def logDbg(self, msg: str = "") -> None:
        """
            Logs debug message.
            
            Args:
                msg : Message to be logged.
        """
        self.__logger.debug(self._addCallerFunctionsName(msg))
    

    def logInf(self, msg: str = "") -> None:
        """
            Logs info message.
            
            Args:
                msg : Message to be logged.
        """
        self.__logger.info(self._addCallerFunctionsName(msg))
    

    def logWng(self, msg: str = "") -> None:
        """
            Logs warning message.
            
            Args:
                msg : Message to be logged.
        """
        self.__logger.warning(self._addCallerFunctionsName(msg))
    

    def logErr(self, msg: str = "") -> None:
        """
            Logs error message.
            
            Args:
                msg : Message to be logged.
        """
        self.__logger.error(self._addCallerFunctionsName(msg))
    
    
    def logCrt(self, msg: str = "") -> None:
        """
            Logs critical message.
            
            Args:
                msg : Message to be logged.
        """
        self.__logger.critical(self._addCallerFunctionsName(msg))


def test_logger_initialization_no_duplicate_handlers():
    """
    Test that DataLogger initializes a logger with a handler.
    """
    logger_name = "test_logger_init"
    dl1 = DataLogger(name=logger_name)
    dl2 = DataLogger(name=logger_name)
    
    logger = logging.getLogger(logger_name)
    # Only one handler should exist despite creating two DataLogger instances
    assert len(logger.handlers) == 1
    assert logger.level == logging.DEBUG
    assert not logger.propagate


def test_add_caller_function_name_disabled():
    """
    Test that _addCallerFunctionsName returns the message unchanged when disabled.
    """
    dl = DataLogger(log_caller_fn=False)
    result = dl._addCallerFunctionsName("mymsg")
    assert result == "mymsg"


@pytest.mark.parametrize("method_name,level", [
    ("logDbg", "debug"),
    ("logInf", "info"),
    ("logWng", "warning"),
    ("logErr", "error"),
    ("logCrt", "critical"),
])
def test_logging_methods_call_correct_logger(method_name, level):
    """
    Test that each logging method calls the corresponding logger method with the message.
    Uses unittest.mock to patch the internal logger.
    """
    dl = DataLogger(log_caller_fn=False)
    
    # Patch the internal logger
    with patch.object(dl._DataLogger__logger, level) as mock_log:
        getattr(dl, method_name)("test message")
        mock_log.assert_called_once_with("test message")


def test_logging_includes_caller_function_name(monkeypatch):
    """
    Test that logged message includes the caller function name when log_caller_fn is True.
    """
    dl = DataLogger(log_caller_fn=True)
    
    called_msg = None

    def fake_debug(msg):
        nonlocal called_msg
        called_msg = msg

    # Replace logger.debug with fake.
    monkeypatch.setattr(dl._DataLogger__logger, "debug", fake_debug)

    def sample_function():
        dl.logDbg("hello")
    
    sample_function()
    assert "sample_function" in called_msg
    assert "hello" in called_msg
