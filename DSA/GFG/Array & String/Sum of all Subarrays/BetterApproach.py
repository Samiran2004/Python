class BetterApproachSolution:
    def subarraySum(self, arr):
        n = len(arr)
        res = 0

        for i in range(n):
            res += arr[i] * (i + 1) * (n - i)

        return res