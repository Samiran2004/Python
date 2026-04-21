from typing import List


class BruteForceSolution:
    def groupAnagrams(self, strs: List[str]):
        n = len(strs)
        visited = [False] * n
        result = []
        
        # Helper function to check two strings are anagram or not...
        def isAnagram(s1: str, s2: str):
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)
        
        for i in range(n):
            if visited[i]:
                continue
            
            curr_group = [strs[i]]
            visited[i] = True
            
            for j in range(i + 1, n):
                if not visited[j]:
                    if isAnagram(s1=strs[i], s2=strs[j]):
                        curr_group.append(strs[j])
                        visited[j] = True
            result.append(curr_group)
        return result