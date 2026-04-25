from math import sqrt

def calculate_factor(num: int)-> list:
    result = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

def brute_force(num: int)-> list:
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)
    return sorted(result)

num = int(input("Enter the number: "))
print(calculate_factor(num=num))
print(brute_force(num=num))
