def arraySign(nums)-> int:
    product = 1
    for num in nums:
        product *= num
    def signFunc(product: int)-> int:
        if product == 0:
            return 0
        elif product < 0:
            return -1
        else:
            return 1
    return signFunc(product=product)

nums = list()
size = int(input("Enter the size of the array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    nums.append(data)
print(arraySign(nums=nums))
