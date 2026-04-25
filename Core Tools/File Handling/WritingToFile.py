with open("output.txt", "w") as file:  # "w" mode overwrit the file
    file.write("This is a log entry.\n")

with open("output.txt", "a") as file:
    file.write("Another log entry using 'a' method.\n")