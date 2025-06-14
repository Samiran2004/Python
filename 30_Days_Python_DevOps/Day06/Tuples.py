my_tuple = (1, 2, 'Samiran', 'Zephyrus') # Tuple is immutable
print(f"my_tuple: {my_tuple}")

first_element = my_tuple[0] # First element
print(f"first_element: {first_element}")

tuple_length = len(my_tuple) # length of the tuple
print(f"Length of the tuple: {tuple_length}")

coordinate = (2, 4)
x, y = coordinate # Tuple packing and unpacking
print(f"x: {x}, y: {y}")

new_tuple = my_tuple + (3.14, "Guddu")
print(f"new_tuple: {new_tuple}")

is_present = 'Samiran' in my_tuple;
print(is_present)

def getCoordinate():
    return(3, 6)

x,y = getCoordinate()
print(f"x: {x}, y: {y}")

print(f"Type of tuple: {type(my_tuple)}")