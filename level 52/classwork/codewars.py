#1
def get_average(marks):
    return sum(marks) // len(marks)
#2
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"
#3
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])
#4
def cockroach_speed(s):
    return int(s*27.777778)
#5
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]
#6
def square(n):
    return n*n
#7
def remove_every_other(my_list):
    new_list = []
    
    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])
    
    return new_list
#7 V2
def remove_every_other(my_list):
    return my_list[::2]
#7 V3
def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i%2 == 0]
#8
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res
#9
def str_count(strng, letter):
    return strng.count(letter)
#10
def is_even(n): 
    return n % 2 == 0
#11
def move(position, roll):
    return position + roll*2
#12
def get_planet_name(id):
    if id == 1: return "Mercury"
    elif id == 2: return "Venus"
    elif id == 3: return "Earth"
    elif id == 4: return "Mars"
    elif id == 5: return "Jupiter"
    elif id == 6: return "Saturn"
    elif id == 7: return "Uranus"
    elif id == 8: return "Neptune"
#13
def enough(cap, on, wait):
    available = cap - on
    
    if available >= wait: return 0
    return wait - available
#14
def between(a,b):
    return list(range(a, b+1))
#15
