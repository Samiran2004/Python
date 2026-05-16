class BetterApproachSolution:
    def nonRepeatingChar(self, s: str):
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for c in s:
            if freq[ord(c) - ord('a')] == 1:
                return c
        return "$"