class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return self.gcd(a-b, b)
        return self.gcd(a, b-a)