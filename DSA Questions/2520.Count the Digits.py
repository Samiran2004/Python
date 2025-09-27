def countDigits(num: int)-> int:
    count = 0
    n = num
    while n != 0:
        rem = n % 10
        if num % rem == 0:
            count += 1
        n = n // 10
    return count

num = int(input("Enter the number: "))
print(f"The number is: {num}")
print(f"Result: {countDigits(num=num)}")
