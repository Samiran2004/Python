class BetterApproachSolution:
    def characterReplacement(self, s: str, k: int):
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        return max_len