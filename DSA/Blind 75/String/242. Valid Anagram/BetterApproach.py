class BetterApproachSolution:
    def isAnagram(self, s: str, t: str):
        return "".join(sorted(s)) == "".join(sorted(t))