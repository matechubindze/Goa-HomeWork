#----------------------------------------------------
#1
try:
    num1 = float(input("Enter the first number (numerator): "))
    num2 = float(input("Enter the second number (denominator): "))

    if num2 == 0:
        raise ValueError("You can't divide by zero!")

    print("Result:", num1 / num2)

except ValueError as error:
    print("Error:", error)

except:
    print("Please enter valid numbers.")

finally:
    print("Operation complete.")
#-----------------------------------------------------
#2
def apply_to_list(func, values):
    return [func(x) for x in values]

def square(x):
    return x * x

print(apply_to_list(square, [1, 2, 3, 4, 5]))
