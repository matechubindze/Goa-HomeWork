#1
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None
#2
def to_alternating_case(s):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
#3
def sum_str(a, b):
    return str(int(a or "0") + int(b or "0"))
#I Aready Have Other Ones Done In The Past So Thats It