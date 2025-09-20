#Codewars N1
def power_of_two(x):
    numbers = [1, 2]
    while numbers[-1] < x:
        numbers.append(numbers[-1]*2)
    return x in number
#Codewars N2
def row_weights(array):
    team1, team2 = 0, 0

    for i in range(len(array)):
        if i%2 == 0:
            team1+=array[i]
        else:
            team2+=array[i]

    return (team1, team2)
#Codewars N3
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return int((sum([i * i for i in ages])**0.5)/2)
#Codewars N4
def greet(name): 
    r_name = name.capitalize()
    return f"Hello {r_name}!"
