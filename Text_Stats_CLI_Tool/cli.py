import argparse
import string

def getArgs() -> dict[str, any]:
    parser = argparse.ArgumentParser(description = "File Stats")
    
    parser.add_argument("target_file", nargs="?", default = "sample.txt", help = "File to be processed")
    parser.add_argument("chars_to_ignore", nargs="?", default = (string.punctuation + string.whitespace), help = "Characters to be ignored")
    parser.add_argument("words_to_ignore", nargs="?", default = "", help = "Words to be ignored")
    parser.add_argument("--verbose",action = "store_true", help = "Enable verbose output")

    return vars(parser.parse_args())
