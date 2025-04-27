#1
def greet(name):
    print(f"Hello, {name}")

greet("Mate")
##2
def manual_range(start, end, step):
    for number in range(start, end, step):
        if number % 2 == 0:
            print(number)

#3
def manual_len(my_list):
    count = 0
    for _ in my_list:
        count += 1
    print(count)



