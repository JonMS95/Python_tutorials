'''
Tests are meant to be way more exhaustive than the ones in this module. However, we are going
to keep them simple as the current project was built just for educational purposes.
'''

import pytest
from stats import StatsHandler

target_text = "sample.txt"
chars_to_ignore = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"

sh = StatsHandler(target_text, chars_to_ignore)

def testCountingStats() -> None:
    assert sh.getStats()["char_count"] == 240
    assert sh.getStats()["word_count"] == 51
    assert sh.getStats()["line_count"] == 3

def testCharHistStats() -> None:
    assert sh.getStats()["char_hist"]['a'] == 14
    assert sh.getStats()["char_hist"]['d'] == 12
    assert sh.getStats()["char_hist"]['e'] == 33

def testWordHistStats() -> None:
    assert sh.getStats()["word_hist"]["town"]  == 1
    assert sh.getStats()["word_hist"]["the"]   == 9
    assert sh.getStats()["word_hist"]["of"]    == 4