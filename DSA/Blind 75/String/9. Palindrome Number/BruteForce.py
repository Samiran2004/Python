class BruteForceSolution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return True
        n = x
        res = 0
        while n > 0:
            rem = n % 10
            res = res * 10 + rem
            n = n // 10
        
        return res == x