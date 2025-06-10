a = [1, 2, 3]
print(a)
a.append(4) # Add 4 to the end of the list
print(a)

# Create a copy of the list
b = a.copy()
print(b)

# Remove all elements from the list
a.clear()
print(a)

# Count occurrence of 2 in the list
a = [1, 2, 3, 2, 4, 2, 5]
print(a.count(2))

# Extend list a by adding elements from list [3, 4]
a = [1, 2]
a.extend([3, 4])
print(a)

# Find the index of 2 in the list
a = [1, 3, 4, 5, 2, 6, 7]
print(a.index(2))

# Insert 2 at index 1
a = [1, 2]
a.insert(1, 3)
print(a)

# Remove and return the last element in the list
a = [1, 2, 3]
a.pop()
print(a)

# Remove the first occurrence of 2
a = [1, 2, 3, 2]
a.remove(2)
print(a)

# Reverse the list order
a = [1, 2, 3, 4]
a.reverse()
print(a)

# Sort the list in ascending order
a = [4, 5, 7, 6, 1, 2, 8]
a.sort()
print(a)