'''
Stats-generating class. Its constructor takes a path to a target file, and a set of
characters and words to be ignored. It generates some insightful stats in exchange. 
'''

import re
from io_utils import getFileLines

class StatsHandler:
    stats: dict = {
        "char_count"    : 0 ,
        "word_count"    : 0 ,
        "line_count"    : 0 ,
        "char_hist"     : {},
        "word_hist"     : {},
    }

    file_path: str              = ""
    chars_to_ignore: str        = ""
    words_to_ignore: list[str]  = []

    word_regex: str = r'\b\w+\b'
    

    def __init__(self, file_path: str, chars_to_ignore: str = "", words_to_ignore: list[str] = []):
        self.file_path          = file_path
        self.chars_to_ignore    = chars_to_ignore
        self.words_to_ignore    = words_to_ignore
        self.processTargetFile()


    def countCharsCb(self) -> None:
        self.stats["char_count"] += 1


    def addLineCharsToStatsCb(self, c: str) -> None:
        if c not in self.stats["char_hist"].keys():
            self.stats["char_hist"][c] = 0
        self.stats["char_hist"][c] += 1


    def charStatsHandler(self, target_line: str) -> None:
        for c in target_line:
            if c not in self.chars_to_ignore:
                self.countCharsCb()
                self.addLineCharsToStatsCb(c)


    def isLineIgnorable(self, target_line: str) -> bool:
        return all(c in self.chars_to_ignore for c in target_line)


    def countLines(self, target_lines: list[str]) -> None:
        self.stats["line_count"] = sum(1 for line in target_lines if not self.isLineIgnorable(line))


    def countWordsInLineCb(self) -> None:
        self.stats["word_count"] += 1

    
    def addLineWordsToStatsCb(self, w: str) -> None:
        if w not in self.stats["word_hist"].keys():
            self.stats["word_hist"][w] = 0
        self.stats["word_hist"][w] += 1


    def wordStatsHandler(self, target_line: str) -> None:
        words: list[str] = re.findall(self.word_regex, target_line)

        for w in words:
            if w not in self.words_to_ignore:
                self.countWordsInLineCb()
                self.addLineWordsToStatsCb(w)


    def processTargetFile(self) -> None:
        lines = getFileLines(self.file_path)

        self.countLines(lines)

        for line in lines:
            self.charStatsHandler(line)
            self.wordStatsHandler(line)
    

    def getStrCharHist(self) -> str:
        ret = "Character histogram:\n"
        
        hist = self.stats["char_hist"]
        keys = sorted(hist.keys())

        for key in keys:
            ret += (repr(key)[1:-1] + " : " + str(hist[key]) + '\n')
        
        return ret


    def getStrWordHist(self) -> str:
        ret = "Word histogram:\n"
        
        hist = self.stats["word_hist"]
        keys = sorted(hist.keys())

        for key in keys:
            ret += (key + " : " + str(hist[key]) + '\n')
        
        return ret


    def __str__(self) -> str:
        c_cnt: str = f"Char count: {self.stats['char_count']}\n"
        w_cnt: str = f"Word count: {self.stats['word_count']}\n"
        l_cnt: str = f"Line count: {self.stats['line_count']}\n"
        
        c_hst: str = self.getStrCharHist()
        w_hst: str = self.getStrWordHist()
            
        return (c_cnt + w_cnt + l_cnt + c_hst + w_hst)


    def getStats(self) -> dict[str, any]:
        return self.stats
    

    def __repr__(self) -> str:
        return str(self.stats)