from collections import deque

llist = deque("abcde")
print(llist)

# Add to right (end)
llist.append("f")
print(llist)

# Remove from right
last = llist.pop()
print(last)
print(llist)

# Add to left (beginning)
llist.appendleft("z")
print(llist)

# Remove from left
first = llist.popleft()
print(first)
print(llist)