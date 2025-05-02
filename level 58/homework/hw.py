add_five = lambda x: x + 5

multiply = lambda x, y: x * y

is_even = lambda x: x % 2 == 0

c_to_f = lambda c: list(map(lambda x: (x * 9/5) + 32, c))

starts_with_a = lambda s: s.startswith('A')

add_10 = list(map(lambda x: x + 10, [1, 2, 3, 4]))

to_upper = list(map(lambda s: s.upper(), ['apple', 'banana', 'cherry']))

lengths = list(map(lambda s: len(s), ['hello', 'world', 'python']))

squares = list(map(lambda x: x ** 2, [1, 2, 3, 4]))

int_to_str = list(map(str, [1, 2, 3, 4]))

greetings = list(map(lambda name: "Hello " + name, ['Alice', 'Bob', 'Charlie']))

subtract_5 = list(map(lambda x: x - 5, [10, 20, 30]))

multiply_3 = list(map(lambda x: x * 3, [2, 4, 6]))

c_to_f_map = list(map(lambda c: (c * 9/5) + 32, [0, 20, 37, 100]))

greater_than_50 = list(map(lambda x: x > 50, [10, 60, 45, 100]))
