#1
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is {result}")
    
    except ValueError:
        print("Error: Please enter valid numeric input.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
divide_numbers()
#2
def access_dictionary_key():
    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

    try:
        key = input("Enter the key you want to access: ")
        value = my_dict[key]
        print(f"The value for '{key}' is: {value}")
    
    except KeyError:
        print(f"Error: The key '{key}' does not exist in the dictionary.")
access_dictionary_key()
#3
def convert_to_integer():
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        print(f"You entered the integer: {number}")
    
    except ValueError:
        print("Error: That is not a valid integer.")
convert_to_integer()
#4
def greet():
    print("Hello! Welcome!")

def call_function(func):
    func()

call_function(greet)
#5
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

# Example usage:
times_three = multiplier(3)
result = times_three(10)
print(result)  # Output: 30



