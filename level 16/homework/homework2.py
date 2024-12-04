correct_username = "Mate"
correct_password = "1234"
 
user_input = input("Enter Username:  ")
user_password = input("Enter Password:  ")
while (user_input != correct_username) or (user_password != correct_password):
    print("Incorrect")
    user_input1 = input("Enter Useraname: ")
    user_password = input("Enter Password")
    print("correct password")
    print("correct username")