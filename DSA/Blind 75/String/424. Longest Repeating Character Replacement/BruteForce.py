class BruteForceSolution:
    def characterReplacement(self, s: str, k: int):
        max_len = 0
        
        for i in range(len(s)):
            freq = [0] * 26
            max_freq = 0
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('A')] += 1
                max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])
                window_len = j - i + 1
                
                replace = window_len - max_freq
                
                if replace <= k:
                    max_len = max(max_len, window_len)
        
        return max_len