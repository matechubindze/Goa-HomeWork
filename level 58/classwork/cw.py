capitalize_string = lambda s: s.capitalize()

print(capitalize_string("hello"))
print(capitalize_string("world"))
print(capitalize_string("python"))
#CW2
print(lambda x:x*2)(int(input("Enter Number:  ")))
#CW3
initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_map = map(lambda x: x**2, initial_list)
print("Map object:", squared_map)
print("Squared list:", list(squared_map))
