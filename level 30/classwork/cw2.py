def manual_find(main_string, str_to_find):
    if str_to_find in main_string:
        return main_string.index(str_to_find)
    return -1

print(manual_find("hello world", "world"))
print(manual_find("hello world", "python"))

