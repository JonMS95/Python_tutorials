from cli import getArgs
from stats import StatsHandler
from stream_logger import StreamLogger
from logging import DEBUG as dbg

def main():
    logger = StreamLogger(__name__, dbg)
    
    parsed_args = getArgs()
    
    logger.logDbg(f"Target file: {parsed_args['target_file']}")
    logger.logDbg(f"Characters to ignore: {'n/a' if parsed_args['chars_to_ignore'] == '' else repr(parsed_args['chars_to_ignore'])[1:-1]}")
    logger.logDbg(f"Words to ignore: {'n/a' if parsed_args['words_to_ignore'] == '' else parsed_args['words_to_ignore']}")
    
    try:
        stats_handler = StatsHandler(parsed_args["target_file"], parsed_args["chars_to_ignore"], parsed_args["words_to_ignore"])
    except FileNotFoundError as fne:
        logger.logErr(f"Missing file: {fne}")
    except Exception as e:
        logger.logErr(f"Exception found: {e}")
    else:
        logger.logInf(stats_handler)
    finally:
        logger.logDbg("Closing main program")


if __name__ == "__main__":
    main()