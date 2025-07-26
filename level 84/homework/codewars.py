<<<<<<< HEAD
#1
def reverse_letter(string):
    return ''.join([ch for ch in string[::-1] if ch.isalpha()])
#2
def gimme(arr):
    return arr.index(sorted(arr)[1])
#3
def angle(n):
    return (n - 2) * 180
#4
def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    return sorted_ages[-2:]
=======
#1
def reverse_letter(string):
    return ''.join([ch for ch in string[::-1] if ch.isalpha()])
#2
def gimme(arr):
    return arr.index(sorted(arr)[1])
#3
def angle(n):
    return (n - 2) * 180
#4
def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    return sorted_ages[-2:]
>>>>>>> 443982d2b36529a17d4928d69650d932a85e0f7b
