class Solutions:
    def isSubSequence(self, s1: str, s2: str):
        n, m = len(s1), len(s2)
        i, j = 0, 0

        while (i < n and j < m):
            if (s1[i] == s2[j]):
                i += 1
            j += 1

        return i == n