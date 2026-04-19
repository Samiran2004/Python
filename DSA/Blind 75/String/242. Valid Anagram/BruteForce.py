class BruteForceSolution:
    def isAnagram(self, s: str, t: str):
        hash_mapS = {}
        hash_mapT = {}
        
        if len(s) != len(t):
            return False
        
        for c in s:
            hash_mapS[c] = hash_mapS.get(c, 0) + 1
        
        for c in t:
            hash_mapT[c] = hash_mapT.get(c, 0) + 1
        
        return hash_mapS == hash_mapT