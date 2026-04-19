class OptimalApproachSolution:
    def lengthOfLongestSubstring(self, s: str):
        maxi = 0
        
        for i in range(len(s)):
            my_set = set()
            for j in range(i, len(s)):
                if s[j] in my_set:
                    break
                my_set.add(s[j])
                curr_len = j - i + 1
                maxi = max(maxi, curr_len)
        
        return maxi