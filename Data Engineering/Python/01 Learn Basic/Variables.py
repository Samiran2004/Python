age = 25
height = 5.9
z = 3 + 4j
print(f"Age: {age} and type of age: {type(age)}")
print(f"Height: {height} and type of height: {type(height)}")
print(f"Z: {z} and type of z: {type(z)}")


name = "Samiran"
print(name.upper())
print(name.capitalize())
print(name.lower())
print(name[0])


# List (mutable)
fruits = ["apple", "banana"]
print(fruits)
fruits.append("cherry")
print(fruits)

# Tuple (immutable)
point = (10, 20)
print(point)

for i in range(3):
    print(i)
    

person = {
    "name": "Samiran",
    "age": 22,
}
print(person)
person["city"] = "Kolaghat"
print(person)
print(person["name"])

# Set (unique, unordered)
nums = {1, 2, 3, 4, 2}
print(nums)

# Boolean
is_adult = True
result = None
print(type(is_adult))
print(type(result))