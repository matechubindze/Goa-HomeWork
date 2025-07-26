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
