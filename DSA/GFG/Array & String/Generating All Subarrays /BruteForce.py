class BruteForceSolution:
    def getSubArrays(self, arr):
        result = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subArray = []
                for k in range(i, j+1):
                    subArray.append(arr[k])
                result.append(subArray)

        return result