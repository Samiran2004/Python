name = "Samiran Samanta"
age = 20
height = 5.8
fruits = ["apple", "orange", "banana"]
coordinates = (10,20)
person_info = {
    "name": name,
    "Age": age,
    "Height": height
}
print(f"Typeof name: {type(name)}")
print(f"Typeof age: {type(age)}")
print(f"Typeof height: {type(height)}")
print(f"Typeof fruits: {type(fruits)}")
print(f"Typeof coordinates: {type(fruits)}")
print(f"Typeof person_info: {type(person_info)}")

print(f"name: {name}")
print(f"age: {age}")
print(f"height: {height}")
print(f"fruits: {fruits}")
print(f"coordinates: {coordinates}")
print(f"person_info: {person_info}")

for fruit in fruits:
    print(f"{fruit}")

for coordi in coordinates:
    print(coordi)

for info in person_info:
    print(info)

for key, value in person_info.items():
    print(f"{key}: {value}")