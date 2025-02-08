def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum([3, 7, 2, 9, 5]))
