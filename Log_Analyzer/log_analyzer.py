'''
This is just a tiny project comprising the lessons taken on the following chapters:
    ·Command_Line_Arguments
    ·Control_Structures
    ·Error_Handling
    ·File_IO
    ·First_Script
    ·Functions_Scope_and_Arguments
    ·Modules
    ·Variables_and_Data_Types
'''

import argparse
import re   # Short for "regular expression"

def parseInput() -> dict:
    """
    Parses input parameters.

    Args:
        None

    Returns:
        dict: Parsed parameters as dict.
    """
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("target_file", help="File to be processed")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return vars(parser.parse_args())

def getLinesFromFile(file_path: str) -> list:
    """
    Retrieves file as list of strings (line by line).

    Args:
        file_path (str): Path to target file

    Returns:
        list: List of strings, one per line.
    """
    ret = []
    try:
        with open(file_path, 'r') as file:
            ret = file.readlines()
    except FileNotFoundError as fee:
        print(f"File not found error caught: {fee}")
    finally:
        return ret

def analyzeLine(line: str, data: dict, word_hist: dict) -> None:
    """
    Analyze each line.

    Args:
        line (str): A string to be analyzed.
        data (dict): A dictionary comprising relevant fields to be taken into account.
        word_hist (dict): A histogram to annotate each word's frequency.

    Returns:
        None
    """
    words = re.findall(r'\b\w+\b', line)
    data["words"] += len(words)
    data["characters"] += len(line)
    for word in words:
        if word not in word_hist.keys():
            word_hist[word] = 0
        word_hist[word] += 1

def getTopFiveFreqWords(word_hist: dict) -> list:
    """
    Gets top five most frequent words from histogram.

    Args:
        word_hist (dict): A histogram storing words as keys and integers as each word's number of appearances in a text.

    Returns:
        list: A list of the 5 keys with highest values.
    """
    sort_crit = lambda x : x[1]
    sorted_pair_list = sorted(word_hist.items(), key=lambda x : x[1], reverse=True)
    sorted_trimmed_pair_list = sorted_pair_list[0:5]
    sorted_hist = dict(sorted_trimmed_pair_list)
    return list(sorted_hist.keys())

def analyzeFile(file_path: str) -> dict:
    """
    Analyzes target file returning a dict comprising:
        ·File name
        ·Number of lines
        ·Number of words
        ·Number of characters
        ·Top 5 most frequent words

    Args:
        file_path (str): Path to target file.

    Returns:
        dict: A dictionary object including relevant information about the provided file.
    """
    lines = getLinesFromFile(file_path)
    word_hist = {}
    data =  {
            "file_name" :   file_path   ,
            "lines"     :   len(lines)  ,
            "words"     :   0           ,
            "characters":   0           ,
            }
    for line in lines:
        analyzeLine(line, data, word_hist)
    data["top_5_freq_words"] = getTopFiveFreqWords(word_hist)
    return data

def main():
    """
    Main function.

    Args:
        None

    Returns:
        None
    """
    input_arguments = parseInput()
    analyzed_data = analyzeFile(input_arguments["target_file"])
    
    if not input_arguments["verbose"]:
        print(analyzed_data)
    else:
        print(f"File name: {analyzed_data['file_name']}")
        print(f"Number of lines: {analyzed_data['lines']}")
        print(f"Number of words: {analyzed_data['words']}")
        print(f"Number of characters: {analyzed_data['characters']}")
        print(f"Top 5 most frequent words: {analyzed_data['top_5_freq_words']}")

if __name__ == "__main__":
    main()