class OptimalApproachSolution:
    def getSubArrays(self, arr):
        result = []
        for i in range(len(arr)):
            current = []
            for j in range(i, len(arr)):
                current.append(arr[j])
                result.append(current.copy())

        return result