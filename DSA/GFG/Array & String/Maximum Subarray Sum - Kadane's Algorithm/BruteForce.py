class BruteForceApproachSolution:
    def maxSubarraySum(self, arr):
        res = 0
        for i in range(len(arr)):
            currSum = 0
            for j in range(i, len(arr)):
                currSum += arr[j]
                res = max(res, currSum)

        return res