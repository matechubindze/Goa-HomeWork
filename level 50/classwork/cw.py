try:
    num = 10
    raise TypeError("This is a TypeError example.")
except TypeError as e:
    print("Caught an error:", e)

def get_user_name():
    try:
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty.")
        
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("Names must contain only letters.")
        
        print("Hello,", first_name, last_name + "!")
    
    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

get_user_name()
