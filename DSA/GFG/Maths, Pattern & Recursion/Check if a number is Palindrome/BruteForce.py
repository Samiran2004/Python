class BruteForceSolution:
    def isPalindrome(self, n: int):
        reverse = 0

        x = abs(n)

        while x != 0:
            rem = x % 10
            reverse = reverse * 10 + rem
            x //= 10

        return reverse == abs(n)