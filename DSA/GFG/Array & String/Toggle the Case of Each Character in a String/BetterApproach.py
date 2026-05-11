class BetterApproachSolution:
    def toggleCase(self, s: str):
        n = len(s)

        for i in range(n):
            if 'a' <= s[i] <= 'z':
                s[i] = chr(ord(s[i]) - 32)
            elif 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i]) + 32)
        return s