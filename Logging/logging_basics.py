'''
Print is fine for quick debugging but:
·It can easily beturned off in production.
·It does not show where messages come from.
·It does not show severity levels either (info, warning, error, debug...).

Use logging built-in library to fix it.

Logger's hierarchy is the following:
DEBUG < INFO < WARNING < ERROR < CRITICAL

Therefore, any level on the list above will lead to messages of such level to
be logged as well as all levels rightwards. For instance, if level is equal to
INFO (see below), then INFO, WARNING, ERROR and CRITICAL messages will be
logged, but not DEBUG. Fun fact: every logging level is associated to a number:
10, 20, 30, 40, 50, respectively.
'''

import logging

def log_basics() -> None:
    # Configure logging (only needs to be done once per module).
    logging.basicConfig(level=logging.INFO)

    logging.debug("This is a debug message")    # Won't be printed since logger's level is one step below.
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

def main():
    log_basics()

if __name__ == "__main__":
    main()

'''
This lesson has implicitly used Python's root logger (the default global logger
that logging module provides). This topic will be further discussed in other
lessons.
'''