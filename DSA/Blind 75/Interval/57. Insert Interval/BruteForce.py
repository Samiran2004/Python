from typing import List


class BruteForceSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        res = []
        len_interval = len(intervals)
        start, end = newInterval[0], newInterval[1]
        ind = 0

        while ind < len_interval and start > intervals[ind][1]:
            res.append(intervals[ind])
            ind += 1

        while ind < len_interval and end >= intervals[ind][0]:
            start = min(start, intervals[ind][0])
            end = max(end, intervals[ind][1])
            ind += 1

        res.append([start, end])

        while ind < len_interval:
            res.append(intervals[ind])
            ind += 1

        return res