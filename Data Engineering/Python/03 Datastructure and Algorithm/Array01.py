import array as arr

a = arr.array('d', [1.1, 2.1, 3.1, 4.1, 5.1])

print(a[0])
print(a[1])
print(a[-1])
print(a[-2])

# Slicing [start:end:step]
print(a[0:3])
print(a[1:4])
print(a[::2])
print(a[::-1])