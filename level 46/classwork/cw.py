#1
def manual_list(start, end, step, user_num):
    result = [i for i in range(start, end, step) if i > user_num]
    return result

print(manual_list(1, 10, 2, 3))
print(manual_list(5, 20, 3, 10))
print(manual_list(0, 30, 5, 15))
#2
numbers = [n for n in range(1, 101) if (n % 3 == 0 and n % 5 != 0) or (n % 5 == 0 and n % 3 != 0)]
print(numbers)
