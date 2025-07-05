#1
def stray(arr):
    if arr[0] == arr[1]:
        common = arr[0]
    else:
        return arr[0] if arr[2] == arr[1] else arr[1]
    for x in arr:
        if x != common:
            return x
#2
def solution(nums):
    return sorted(nums) if nums else []
#3
def position(alphabet):
    return f"Position of alphabet: {ord(alphabet.lower()) - 96}"
#4
def break_chocolate(n, m):
    return max(n * m - 1, 0)
#5
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
