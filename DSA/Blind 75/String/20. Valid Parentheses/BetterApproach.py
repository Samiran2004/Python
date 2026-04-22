class BetterApproachSolution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 0:
            return False
        
        stack = []
        map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if not stack or map[char] != stack.pop():
                    return False
        
        return not stack