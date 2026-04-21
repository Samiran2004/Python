import collections
from typing import List


class BetterApproachSolution:
    def groupAnagrams(self, strs: List[str]):
        anagram_map = collections.defaultdict(list)
        
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        
        return list(anagram_map.values())