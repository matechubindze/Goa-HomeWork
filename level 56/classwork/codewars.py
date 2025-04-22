#1
def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)
#2
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
#3
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"
#4
def reverse_list(l):
    return l[::-1]
#5
def odd_count(n):
    return n//2
#6
def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a
#7
def greet(language):
    all_lang = [ 
        ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
    ]
    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"
#8
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
#9
def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]
#10
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
print(total_goals)
#11
def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
#12
def fix_the_meerkat(arr):
    return arr[::-1]
#13
def find_multiples(n, limit):
    return [i for i in range(n, limit + 1, n)]
#14
def create_aray(n):
    res = []
    i = 1
    while i <= n:
        res +=[i]
        i +=1 
        
