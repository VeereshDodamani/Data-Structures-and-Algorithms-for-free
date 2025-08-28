# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
from typing import List

def groupAnagrams(strs):
    anagrams_dict = defaultdict(list)
    for s in strs:
        count =  [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        anagrams_dict[key].append(s)
    return list(anagrams_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
