class BruteForceApproachSolution:
    def nonRepeatingChar(self, s: str):
        n = len(s)

        for i in range(n):
            found = False
            for j in range(n):
                if s[i] == s[j]:
                    found = True
                    break
            if not found:
                return s[i]

        return "$"