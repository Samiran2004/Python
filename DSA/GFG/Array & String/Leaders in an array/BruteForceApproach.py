class BruteForceApproachSolution:
    def leaders(self, arr):
        result = []
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] < arr[j]:
                    break
            else:
                result.append(arr[i])
        return result