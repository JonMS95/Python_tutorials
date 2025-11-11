'''
Logging can be configured by using various parameters. These parameters
include, but don't limit to:
·File name: file/app name, as string.
·File mode: a/w (append, overwrite).
·Level: log level threshold (DEBUG, INFO...).
·Format: defines log's format. There are several placeholders:
    ·%(asctime)s: timestamp.
    ·%(levelname)s: log level..
    ·%(message)s: the actual message you provide.
    ·%(name)s: logger name.
    ·%(filename)s: source filename.
    ·%(lineno)s: line number.
'''

import logging

def log_to_file() -> None:
    logging.basicConfig(filename="log2file.log", filemode='w',level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("Warning message")

def main():
    log_to_file()

if __name__ == "__main__":
    main()