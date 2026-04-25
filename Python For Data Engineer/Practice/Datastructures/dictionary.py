my_dics = {
    "x": 1,
    "y": 2,
    "z": 3,
    "demo": {
        "a": 1,
        "b": 2,
        "c": 3
    }
}

print(my_dics)
print(type(my_dics))

my_dics["x"] = 10

# my_dics.pop("z")

print(my_dics.keys())
print(my_dics.values())
print(my_dics.items())

print(my_dics['demo']['b'])