class BetterApproachSolution:
    def minWindow(self, s: str, t: str):
        if not s or not t or len(s) < len(t):
            return ""
        
        # Create an array of size 256 to store frequencies of string t
        mapT = [0] * 256
        for char in t:
            mapT[ord(char)] += 1
        
        # Create an array of size 256 for our current sliding window
        mapS = [0] * 256
        
        # Helper function to compare maps in O(1) constant time
        def is_valid():
            for i in range(256):
                if mapT[i] > mapS[i]:
                    return False
            return True
        
        min_len = float('inf')
        start_index = -1
        left = 0
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            mapS[ord(s[right])] += 1
            
            # When the window is valid, try to shrink it from the left
            while is_valid():
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start_index = left
                
                mapS[ord(s[left])] -= 1
                left += 1
        
        if start_index == -1:
            return ""
        return s[start_index : start_index + min_len]