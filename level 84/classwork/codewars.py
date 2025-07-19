#1
Find the stray number
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
#2
def solution(nums):
    if nums is None or nums == []: return []

    nums.sort()
    return nums
#3
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b
#4
def is_anagram(test, original):
    def count_chars(s):
        res = {}
        # {"a": 1}

        for i in s:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1

        return res

    return count_chars(test.lower()) == count_chars(original.lower())
#5
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
#6
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number + 1,step))

