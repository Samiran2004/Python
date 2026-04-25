with open("server.log", "r") as log_file:
    for line in log_file:
        if "WARNING" in line:
            print(line.strip())