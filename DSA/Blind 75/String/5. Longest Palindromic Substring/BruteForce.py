class BruteForceSolution:
    def longestPalindrome(self, s: str):
        if len(s) <= 1:
            return ""
        
        max_len = 0
        max_substring = ""
        
        def isPalindrome(st):
            return st == st[::-1]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_substring = s[i:j+1]
                curr_len = len(curr_substring)
                
                if isPalindrome(curr_substring) and curr_len > max_len:
                    max_len = curr_len
                    max_substring = curr_substring
        
        return max_substring