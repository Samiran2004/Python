class Solutions:
    def rearrange(self, arr):
        posIdx = 0
        negIdx = 0
        posArr = []
        negArr = []
        i = 0

        for num in arr:
            if num >= 0:
                posArr.append(num)
            else:
                negArr.append(num)

        while posIdx < len(posArr) and negIdx < len(negArr):
            if i % 2 == 0:
                arr[i] = posArr[posIdx]
                posIdx += 1
            else:
                arr[i] = negArr[negIdx]
                negIdx += 1
            i += 1

        while posIdx < len(posArr):
            arr[i] = posArr[posIdx]
            posIdx += 1
            i += 1

        while negIdx < len(negArr):
            arr[i] = negArr[negIdx]
            negIdx += 1
            i += 1