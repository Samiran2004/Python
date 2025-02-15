with open("example.txt", "r") as file:
    content = file.read()
    print(content)

## Read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) #Removes extra newline

## Read specific number of characters...
with open("example.txt", "r") as file:
    content = file.read(10) #Read first 10 characters
    print(content)

## Read all lines into a list...
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)