'''
Hints for nested types can be used in Python (dict[int, set[str]], list[list[float]] and so on).

The first example below is based on leetcode's 49th problem: Group Anagrams.
https://leetcode.com/problems/group-anagrams/description/
'''

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ana_map: dict[str, list[str]] = {}
    ret: List[List[str]] = []
    for s in strs:
        if "".join(sorted(s)) not in ana_map.keys():
            ana_map["".join(sorted(s))] = [s]
        else:
            ana_map["".join(sorted(s))].append(s)
    for key in ana_map.keys():
        ret.append(ana_map[key])
    return ret

def testGroupAnagrams() -> None:
    words: list[str] = ["eat","tea","tan","ate","nat","bat"]
    grouped_anagrams = groupAnagrams(words)
    print(f"{words} -> {grouped_anagrams}")

def main():
    testGroupAnagrams()

if __name__ == "__main__":
    main()