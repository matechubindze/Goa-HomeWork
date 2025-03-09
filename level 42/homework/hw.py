#1
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA",
    "profession": "Engineer"
}

print(my_dict.keys())
#2
my_dict = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "color": "Blue",
    "price": 25000
}

print(my_dict.values())
#3
my_dict = {
    "fruit": "Apple",
    "color": "Red",
    "taste": "Sweet",
    "weight": "200g",
    "price": 1.5
}

print(my_dict.items())
#4
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

value = my_dict.get("country", "Key not found")
print(value)
#5
my_dict = {
    "brand": "Nike",
    "category": "Shoes",
    "size": 42,
    "color": "Black"
}

my_dict.clear()
print(my_dict)
