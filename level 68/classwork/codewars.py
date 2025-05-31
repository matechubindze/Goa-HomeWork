#Disemvowel Trolls
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res
#Square Every Digit
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))
#Square Every Digit (Second Solve)
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))
def square_digits(num):
    st = []

    for i in str(num):
        int_i = int(i)
        sq_i = int_i**2
        st.append(str(sq_i))

    return int("".join(st))
#Highest And Lowest
def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"
#Descending Order
    num_str = str(num)
    sorted_digits = sorted(num_str)[::-1]
    sorted_str = ''.join(sorted_digits)
    return int(sorted_str)