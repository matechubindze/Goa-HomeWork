#1
def mouth_size(animal): 
    if animal.lower() == 'alligator':
        return 'small'
    else:
        return 'wide'
#2
def nth_even(n):
    return (n - 1) * 2
#3
def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
#4
def return_five():
    return len("apple")
#5
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]
