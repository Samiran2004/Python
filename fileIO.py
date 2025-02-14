try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    with open("my_file.txt", "w") as file:
        file.write("Hello World!")
except Exception as e:
    print(f"Error: {e}")