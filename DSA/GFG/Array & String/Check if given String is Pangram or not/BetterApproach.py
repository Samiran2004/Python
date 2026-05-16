class BetterApproachSolution:
    def checkPangram(self, s: str):
        visited = [False] * 26

        for c in s:
            if 'A' <= c <= 'Z':
                visited[ord(c) - ord('A')] = True
            elif 'a' <= c <= 'z':
                visited[ord(c) - ord('a')] = True

        for flag in visited:
            if not flag:
                return False
        return True