class OptimizeApproachSolution:
    def leaders(self, arr):
        n = len(arr)
        maxRight = -1

        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, curr)

        return arr