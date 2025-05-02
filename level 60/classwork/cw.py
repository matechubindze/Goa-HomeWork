#1 Exclusive "or" (xor) Logical Operator


def xor(a,b):
    return a!=b



#2 What's the real floor?


def get_real_floor(n):
    if n < 1:
        return n
    elif n < 13:
        return n-1
    elif n > 13:
        return n-2


#3 Filter out the geese


def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if bird not in geese]



#4 Name Shuffler


def name_shuffler(s):
    parts = s.split()
    return f"{parts[1]} {parts[0]}"


#5 Find numbers which are divisible by given number


def divisible_by(numbers, divisor):
    return list(filter(lambda x: x%divisor == 0, numbers))




#6 Lario and Muigi Pipe Problem


def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))


#7 Plural


def plural(n):
    return n == 0 or n > 1


#8 Multiplication table for number


def multi_table(number):
    res = ""
    for i in range(1,11):
        res += f"{i} * {number} = {inumber}\n"
    return res[0:-1]



#9 Super Duper Easy


def problem(a):
    if type(a) == str: return "Error"
    return a50+6

#10 Grasshopper - If/else syntax debug


def check_alive(health):
    if health > 0:
        return True
    else:
        return False


#11 Grasshopper - Basic Function Fixer

def add_five(num):
    total = num + 5
    return total


#12 Grasshopper - Terminal game combat function


def combat(health, damage):
    if health - damage > 0: return health - damage
    return 0

#13 How many lightsabers do you own?


def how_many_light_sabers_do_you_own(*args):
    if len(args) == 0: return 0
    return 18 if args[0] == "Zach" else 0
#14 

