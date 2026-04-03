from typing import List


class BetterApproachSolution:
    def containsDuplicate(self, arr: List[int]):
        seen = set()
        
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False