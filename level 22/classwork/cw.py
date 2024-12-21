a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = int(input("Enter Number: "))

if i >= 0 and i <= 9 or i >= -10 and i <= -1:
    print(a[i])
else:
    print("Invalid index!")
