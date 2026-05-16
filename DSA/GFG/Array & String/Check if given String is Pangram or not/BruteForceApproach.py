from string import ascii_lowercase

class BruteForceApproachSolution:
    def checkPangram(self, s: str):
        for ch in ascii_lowercase:
            found = False

            for i in range(len(s)):
                if ch == (s[i].lower()):
                    found = True
                    break
            if not found:
                return False
        return True