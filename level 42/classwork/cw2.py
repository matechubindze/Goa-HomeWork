
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer",
    "hobby": "Photography"
}

print(data.keys())
print(data.values())
print(data.items())

for k, v in data.items():
    print(k + ": " + str(v))

