#Get The Middle Charachter
def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
#Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")
#Jaden Casing Strings
def to_jaden_case(string):
    string = [i.capitalize() for i in string.split(" ")]
    return " ".join(string)
#Return Text
def solution(text, ending):
    return text.endswith(ending)
#Actual Classwork For Us
def accum(st):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(st))
#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
#No Name
if a==b:
        return a

    if a>b:
        a,b=b,a
    res=0
    for i in range(a,b+1):
        res+=i
    return res
#No Name
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res
#No Name
def maskify(cc):
    if len(cc) <= 4:
        return cc
    return '#' * (len(cc) - 4) + cc[-4:]