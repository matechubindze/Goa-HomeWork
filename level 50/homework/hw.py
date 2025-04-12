try:
    number = int(input("შეიყვანეთ რიცხვი: "))
    print("თქვენ შეიყვანეთ:", number)
except ValueError:
    print("შეცდომა: გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError:
    print("შეცდომა: ცადეთ სიაში არარსებული ინდექსის წაკითხვა.")
try:
    result = "Age: " + 25
except TypeError:
    print("შეცდომა: სტრიქონის რიცხვზე მიმატება შეუძლებელია. გამოიყენეთ str() გარდაქმნა.")
