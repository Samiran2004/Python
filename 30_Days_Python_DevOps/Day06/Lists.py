my_list = [1, 2, 3, "apple", "orange"] # Create a list # List is mutable

print(f"my_list: {my_list}") # Print my_list

first_elm = my_list[0] # Extract the first element of the my_list
print(f"First element of the list: {first_elm}") # Print 1st element

list_length = len(my_list) # Length of the list
print(f"Length of my_list: {list_length}")


## List Manipulation and Common List Operations ##

my_list.append(4) # Adds 4 to the end of the list
print(f"my_list after append: {my_list}")

my_list.remove("apple") # Remove 'apple' from the list
print(f'my_list after removing "apple": {my_list}')

my_list.reverse() # Reverse the list
print(f"my_list after reverse: {my_list}")

subset_list = my_list[1:4] # Slicing the list
print(f"subset_list: {subset_list}")

new_list = my_list + [5, 6] # Concatenation two lists
print(f"new_list: {new_list}")

my_list = [5, 7, 3, 8, 6, 9, 2, 1]
my_list.sort() # Sorting the list. if all elemnts datatypes are same
print(my_list)

my_list = [1, 2, 3, "apple", "orange"]

is_present = 'orange' in my_list # Checks if 'orange' is in the list (True)
print(f"orange is present: {is_present}")