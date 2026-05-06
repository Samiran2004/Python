class BruteForceSolution:
    def isSorted(self, arr) -> bool:
        if len(arr) <= 0:
            return False

        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False

        return True