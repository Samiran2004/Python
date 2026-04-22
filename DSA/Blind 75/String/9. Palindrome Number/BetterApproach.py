class BetterApproachSolution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]