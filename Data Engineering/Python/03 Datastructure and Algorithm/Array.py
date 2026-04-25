import array as arr

int_array = arr.array('i', [1, 2, 3, 4, 5])
print(int_array)

float_array = arr.array('f', [1.1, 1.2, 1.3, 1.4, 1.5])
print(float_array)

char_array = arr.array('w', ['a', 'b', 'c', 'd', 'e'])
print(char_array)

empty_array = arr.array('i')
print(empty_array)