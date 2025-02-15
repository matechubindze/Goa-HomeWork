def no_duplicates(user_list):
    return list(set(user_list))

print(no_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(no_duplicates(["apple", "banana", "apple", "cherry", "banana"]))
print(no_duplicates([10, 20, 30, 10, 40, 50, 20]))