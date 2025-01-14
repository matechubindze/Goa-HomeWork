def manual_swapcase(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        elif "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
print(manual_swapcase("Hello World!"))
