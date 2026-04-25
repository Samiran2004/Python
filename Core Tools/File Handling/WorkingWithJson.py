import json

with open("config.json", "r") as json_file:
    data = json.load(json_file)
    print(data["description"])

## Writing JSON Configuration
data = {
    "database": "mysql",
    "user": "admin",
    "password": "root"
}
with open("config2.json", "w") as file:
    json.dump(data, file, indent=4)