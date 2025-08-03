my_list = [1, 2, 3, 4, 5]

# def square(x):
#     res_list = [i*i for i in x]
#     print(res_list)

# square(my_list)

def square(x):
    return x*x

result = list(map(square, my_list))

print(result)