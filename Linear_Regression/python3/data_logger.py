'''
Logging module. A class has been designed just in case different instances are required
(to be called from different modules).
'''

import logging

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

    def __init__(self, name: str = __name__, level: int = logging.DEBUG):
        """
            Initializer logger object (constructor method).
            
            Args:
                name    : Logger's target name.
                level   : Logger's level (the closer to DEBUG / lower, the more detailed the output will be).
        """
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter(self.__log_format))

        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(level)

        self.__logger.addHandler(self.handler)
    

    def logDbg(self, msg: str = "") -> None:
        """
            Logs debug message.
            
            Args:
                msg : Message to be logged.
        """

        self.__logger.debug(msg)
    

    def logInf(self, msg: str = "") -> None:
        """
            Logs info message.
            
            Args:
                msg : Message to be logged.
        """
        
        self.__logger.info(msg)
    

    def logWng(self, msg: str = "") -> None:
        """
            Logs warning message.
            
            Args:
                msg : Message to be logged.
        """
        
        self.__logger.warning(msg)
    

    def logErr(self, msg: str = "") -> None:
        """
            Logs error message.
            
            Args:
                msg : Message to be logged.
        """
        
        self.__logger.error(msg)
    
    
    def logCrt(self, msg: str = "") -> None:
        """
            Logs critical message.
            
            Args:
                msg : Message to be logged.
        """
        
        self.__logger.critical(msg)
        