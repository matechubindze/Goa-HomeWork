# 2) Print your name
print("John Doe")

# 3) Print a favorite quote
print('"The only limit to our realization of tomorrow is our doubts of today."')

# 4) Print multiple lines
print("Roses are red")
print("Violets are blue")
print("Coding is fun, and so are you!")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols
print("*")
print("**")
print("***")
print("****")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print(num_int)

# 8) Add two floats
a = 3.5
b = 2.5
print(a + b)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Print data types
x = 10
y = "Python"
z = 3.14
print(type(x))
print(type(y))
print(type(z))

# 11) User input and type conversion
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year’s age
age = int(input("How old are you? "))
print("Next year, you'll be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 15) Favorite color
color = input("What's your favorite color? ")
print("Your favorite color is", color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("You are not tall enough.")

# 17) Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
word = "Python"
for letter in word:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(total)

# 20) Print a multiplication table (1 to 5)
for i in range(1, 6):
    print("2 x", i, "=", 2 * i)

# 21) Print all even numbers between 2 and 20 (inclusive)
for i in range(2, 21, 2):
    print(i)

# 22) Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total)

# 24) Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print all odd numbers between 1 and 10
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1
# 27) Print all elements of a list
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)

# 28) Find the length of a list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# 29) Access a specific element from the list
my_list = [10, 20, 30, 40]
print(my_list[1])

# 30) Add an element to the list
my_list = ["red", "green", "blue"]
my_list.append("yellow")
print(my_list)

# 31) Remove an element from the list
my_list = ["dog", "cat", "bird"]
my_list.remove("cat")
print(my_list)

# 32) Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

# 33) Create a list of even numbers
even_numbers = [x for x in range(2, 11) if x % 2 == 0]
print(even_numbers)

# 34) Filter odd numbers from a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = [x for x in nums if x % 2 != 0]
print(odds)

# 35) Convert a list of strings to uppercase
words = ["hello", "world", "code"]
upper_words = [word.upper() for word in words]
print(upper_words)

# 36) Create a list of numbers squared if they are divisible by 2
numbers = [1, 2, 3, 4, 5]
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print(squared_evens)

# 37) Function to greet a user
def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Bob")

# 38) Function to add two numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 4))

# 39) Function to check if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(7))

# 40) Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

print(rectangle_area(6, 4))

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("coding"))

# 42) Create and print a tuple
my_tuple = (7, "hello", 3.5)
print(my_tuple)

# 43) Access an element in a tuple
sample_tuple = (100, 200, 300)
print(sample_tuple[1])

# 44) Find the length of a tuple
sample_tuple = (1, 2, 3, 4, 5)
print(len(sample_tuple))

# 45) Concatenate two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

# 46) Check if an item exists in a tuple
my_tuple = (5, 10, 15)
if 10 in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# 48) Check if an element is in a set
my_set = {1, 2, 3}
if 2 in my_set:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
my_set = {"red", "blue"}
my_set.add("green")
print(my_set)

# 50) Remove an element from a set
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# 52) Create and print a dictionary
person = {"name": "Alice", "age": 30}
print(person)

# 53) Access a value by key
print(person["name"])

# 54) Add a new key-value pair to a dictionary
person["city"] = "Paris"
print(person)
