
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if num1 > num2:
    print(my_list[num2:num1])
elif num2 > num1:
    print(my_list[num1:num2])
else:
    print("Try Again With Different Number")
