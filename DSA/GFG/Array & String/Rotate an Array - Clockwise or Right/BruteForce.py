class BruteForceSolution:
    def rotateArr(self, arr, d):
        n = len(arr)

        for _ in range(d):
            last = arr[n - 1]
            for i in range(n - 1, 0, -1):
                arr[i] = arr[i - 1]
            arr[0] = last