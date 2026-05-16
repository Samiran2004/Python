from typing import List


class BetterApproachSolution:
    def findMajority(self, arr: List[int]):
        n = len(arr)

        elm1, elm2 = -1, -1
        count1, count2 = 0, 0

        for elm in arr:
            if elm == elm1:
                count1 += 1
            elif elm == elm2:
                count2 += 1
            elif count1 == 0:
                elm1 = elm
                count1 += 1
            elif count2 == 0:
                elm2 = elm
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        count1, count2 = 0, 0

        for elm in arr:
            if elm1 == elm:
                count1 += 1
            if elm2 == elm:
                count2 += 1
        if count1 > n // 3:
            res.append(elm1)
        if count2 > n // 3 and elm2 != elm1:
            res.append(elm2)
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]

        return res