numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for number in numbers:
    if number == 5:
        break
    print(number)

for number in numbers:
    if number == 5:
        continue
    print(number)