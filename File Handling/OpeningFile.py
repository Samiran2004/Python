file = open("example.txt", "r")  # "r" for read mode
content = file.read()
print(content)
file.close()

## Using <with open> command...
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


"""
'r' → Read (default)
'w' → Write (overwrites file)
'a' → Append (adds data without overwriting)
'x' → Create (fails if file exists)
'b' → Binary mode (for images, logs)
"""