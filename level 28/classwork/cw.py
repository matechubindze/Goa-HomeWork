def manual_index(key, search):
    i = 0
    while i < len(search):
        if search[i:i+len(key)] == key:
            return i
        i += 1
    return -1
