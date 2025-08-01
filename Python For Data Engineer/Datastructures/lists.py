my_list = [1, 2, "Samiran", "Samanta", ['aa', 'bb', 'cc'], 4, 5, 6]

print(my_list[-3:])

print(len(my_list))

print(my_list[::2])

my_list.append("Hero")

print(my_list) # List's are mutable...

my_list.insert(1, "Hero")

print(my_list)

my_list.pop()
print(my_list)

# print(my_list[::-1])

for i in my_list[::-1]:
    print(i)


my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# new_list = []

# for i in my_list:
#     new_list.append(i * i)

# print(new_list)

new_list = [i * i for i in my_list if(i % 2) == 0]

print(new_list)