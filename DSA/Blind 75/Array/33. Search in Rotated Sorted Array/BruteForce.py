from typing import List


class BruteForceSolution:
    def search(self, nums: List[int], target: int):
        if len(nums) <= 0:
            return -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1