from typing import List


class BruteForceApproachSolution:
    def findMajority(self, arr: List[int]):
        n = len(arr)
        res = []

        for i in range(n):
            count = 0
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    count += 1

            if count >= n // 3:
                if len(res) == 0 or arr[i] != res[0]:
                    res.append(arr[i])

            if len(res) >= 2:
                if res[0] > res[1]:
                    res[0], res[1] = res[1], res[0]
                break
        return res