class BetterApproachSolution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        arr[:] = arr[d:] + arr[:d]