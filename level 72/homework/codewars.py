#1
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()
#2
def is_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] > 0 and sides[0] + sides[1] > sides[2]
#3
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))
#4
def open_or_senior(data):
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open"
        for (age, handicap) in data
    ]
#5
def find_next_square(sq):
    root = sq ** 0.5
    if root == int(root):
        return int((root + 1) ** 2)
    else:
        return -1
