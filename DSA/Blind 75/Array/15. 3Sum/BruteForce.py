from typing import List


class BruteForceSolution:
    def threeSum(self, arr: List[int]):
        st = set()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == 0:
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        st.add(triplet)
        return [list(triplet) for triplet in st]