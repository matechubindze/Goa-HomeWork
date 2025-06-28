#1
def row_sum_odd_numbers(n):
    start_num = 1
    res = []

    for i in range(1, n+1):
        ls = []
        for x in range(i):
            ls.append(start_num)
            start_num += 2
        res.append(sum(ls))

    return res[-1]
#2
def row_sum_odd_numbers(n):
    start = n * n - (n - 1)
    return sum(start + 2 * i for i in range(n))
#3
def row_sum_odd_numbers(n):
    start = n * n - (n - 1)
    return sum(start + 2 * i for i in range(n))
def row_sum_odd_numbers(n):
    return n**3
#4
def printer_error(s):
    errors = sum(1 for c in s if c < 'a' or c > 'm')
    return f"{errors}/{len(s)}"
#5
def printer_error(s):
    valid = "abcdefghijklm"
    res = 0
    for i in s:
        if i not in valid: res += 1

    return f"{res}/{len(s)}"
#6
def reverse_words(text):
    str_list=text.split(" ")
    result = []
    for i in str_list:
        result.append(i[::-1])
    return " ".join(result)