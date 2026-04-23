class BruteForceSolution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def isPalindrome(subStr):
            return subStr == subStr[::-1]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                subString = s[i: j+1]
                if isPalindrome(subStr=subString):
                    count += 1
        
        return count