'''
Using the root's default logger is fine, but in real projects, it's
better to create module-specific loggers by creating a logging class
object (loggers are singleton-like).

Take a look at the example below and all of the provided comments
so as to grasp all the nuances.
'''

import logging

def real_logging() -> None:
    # Define a logger instance with current module's name.
    logger = logging.getLogger(__name__)
    # Set log level.
    logger.setLevel(logging.DEBUG)
    
    # Add a handler. Handler is responsible for sending log records to a particular output.
    # Such output is set as console, but FileHandler, SocketHandler or SMTPHandler could have
    # been used instead.
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # Note that formatter has been defined separatedly in this case.
    handler.setFormatter(formatter)
    
    # Bind previously defined handler to the current logger (a logger supports multiple
    # handlers).
    logger.addHandler(handler)

    logger.debug("Debug message")
    logger.info("Info message")

def main():
    real_logging()

if __name__ == "__main__":
    main()