import json

json_data = '{"name": "Jhon", "age": 30, "city": "New York"}'

data = json.loads(json_data)
print(data)
print(data["name"])
print(data["age"])
print(data["city"])

data["country"] = "USA"
print(data)

data["age"] = 28
print(data)

updated_json_data = json.dumps(data)
print(updated_json_data)

with open ('JSON_Output.json', 'w') as file:
    json.dump(data, file)

with open('JSON_Output.json', 'r') as file:
    data = json.load(file)

print(f"Reading: {data}")