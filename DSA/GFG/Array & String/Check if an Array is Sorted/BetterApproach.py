class BetterApproachSolution:
    def isSorted(self, arr):
        def isSortedHelper(arr, n):
            if n == 0 or n == 1:
                return True
            return (arr[n-1] >= arr[n - 2] and isSortedHelper(arr, n-1))

        n = len(arr)

        return isSortedHelper(arr, n)