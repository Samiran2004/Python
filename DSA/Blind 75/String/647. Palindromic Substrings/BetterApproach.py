class BetterApproachSolution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def palindromeCount(left, right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                result += 1
            return result
        
        for i in range(len(s)):
            count += palindromeCount(i, i)
            count += palindromeCount(i , i+1)
        
        return count