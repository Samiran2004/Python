class BetterApproachSolution:
    def getSubArrays(self, arr):
        result = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                result.append(arr[i:j+1])
        return result