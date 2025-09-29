def xorOperation(n: int, start: int)-> int:
    ans = 0
    nums = [start + n * 2 for n in range(n)]
    for n in nums:
        ans = ans ^ n
    return ans

n = int(input("Enter the value of n: "))
start = int(input("Enter the start value: "))
print(xorOperation(n=n, start=start))
