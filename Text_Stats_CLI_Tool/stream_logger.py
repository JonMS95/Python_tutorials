'''
Logging module. A class has been designed just in case different instances are required
(to be called from different modules).
'''

import logging
from logging import DEBUG as dbg, INFO  as inf, WARNING as wng, ERROR as err, CRITICAL as crt

class StreamLogger:
    log_format: str = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
    logger = None

    def __init__(self, name: str = __name__, level: int = logging.INFO):
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter(self.log_format))

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        self.logger.addHandler(self.handler)
    

    def logDbg(self, msg: str = "") -> None:
        self.logger.debug(msg)
    

    def logInf(self, msg: str = "") -> None:
        self.logger.info(msg)
    

    def logWng(self, msg: str = "") -> None:
        self.logger.warning(msg)
    

    def logErr(self, msg: str = "") -> None:
        self.logger.error(msg)
    
    
    def logCrt(self, msg: str = "") -> None:
        self.logger.critical(msg)
    
