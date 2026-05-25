# python -u "C:\Users\JosephET\Documents\VS Code\Workspace\Testwork\Duplicate.py"

# import numpy as np

# Normal array duplicate --------------------------------------------------------------------------------------------------------
# Method One -> diff in len using set()
nums = [4, 1, 5, 1, 4, 2]

def detect(arr: list[int]) -> bool:
    return len(arr) != len(set(arr))
print('Normal array: diff in len using set() -> ', detect(nums))

# Method Two -> set() loop
def check(arr: list[int]) -> bool:
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
print('Normal array: set() loop -> ', check(nums))

# Method Three -> count()[x]
def checker(arr: list[int]) -> bool:
    return len([x for x in arr if arr.count(x) > 1]) > 0
print('Normal array: count()[x] -> ', checker(nums))

# Method Four -> dict loop
def duplicate(arr: list[int]) -> bool:
    seen = {}
    for num in arr:
        if num in seen:
            return True
        seen[num] = True
    return False
print('Normal array: dict loop -> ', duplicate(nums))

# Method Five -> This requires importing numpy as np therefore to be downloaded using pip
# def numpyy(arr: list[int]) -> bool:
#     return len(np.unique(arr)) != len(arr) 
# print(numpyy(nums))

# 2D array duplicate --------------------------------------------------------------------------------------------------------

# Method One -> set() loop
numbers = [[4, 5, 6], [1, 2, 3], [7, 8, 4]]
def multi(arr: list[list[int]]) -> bool:
    seen = set()
    for row in arr:
        for num in row:
            if num in seen:
                return True
            seen.add(num)
    return False
print('2D array: set() loop -> ', multi(numbers))

# Method Two -> dict loop
def multee(arr: list[list[int]]) -> bool:
    seen = {}
    for row in arr:
        for num in row:
            if num in seen:
                return True
            seen[num] = True
    return False
print('2D array: dict loop -> ', multee(numbers))

# Method Three -> flat_list using set()[x]
def multii(arr: list[list[int]]) -> bool:
   flat_list = [y for x in arr for y in x]
   return len(flat_list) != len(set(flat_list))
print('2D array: flat_list set()[x] -> ', multii(numbers))

#Method Four flat_array using numpy
# def multiD(arr: list[list[int]]):
#     flat_array = np.array(arr).flatten()
#     return len(flat_array) != len(np.unique(flat_array))
# print('2D array: numpy -> ', multiD(numbers))

# Removing normal array duplicate --------------------------------------------------------------------------------------------------------

integers = [4, 1, 8, 5, 4, 2]

# Using loop set() and empty array
def remov(arr: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in arr:
        new_arr = []
        if num not in seen:
            seen.add(num)
            new_arr.append(num)
        if new_arr:
            result.extend(new_arr)
    return result
print('Remove duplicate using set() and new array: ', end='')
for i in remov(integers):
    print(i, end=', ')
print(end=None)

# Using empty array and loop dict
def removed(arr: list[int]) -> list[int]:
    seen = {}
    result = []
    for num in arr:
        new_arr = []
        if num not in seen:
            seen[num] = True
            new_arr.append(num)
        if new_arr:
            result.extend(new_arr)
    return result
print('Remove duplicate using dict and new array: ', end='')
for i in removed(integers):
    print(i, end=', ')

print(end=None)

# Print Normal array duplicate(s) found --------------------------------------------------------------------------------------------------------
integeers = [4, 1, 8, 5, 4, 2, 1]
def printer(arr: list[int]) -> list[int]:
    seen = {}
    result = []
    for num in arr:
        new_arr = []
        if num not in seen:
            seen[num] = True
            new_arr.append(num)
        else:
            result.append(num)
    return result
print('Printing duplicate using dict and new array: ', end='')
for i in printer(integeers):
    print(i, end=', ')

print(end=None)

# Removing 2D array duplicate --------------------------------------------------------------------------------------------------------

# digits = [[4, 2, 5], [7, 1, 9], [1, 6, 8], [4, 0, 3]]
digits = [[4, 2, 5], [7, 1, 9], [1, 6, 4]]

def removal(arr: list[list[int]]) -> list[list[int]]:
    seen = set()
    result = []
    for row in arr:
        new_array = []
        for num in row:
            if num not in seen:
                seen.add(num)
                new_array.append(num)
        if new_array:
            result.append(new_array)
    return result
print('Remove 2D duplicate using set() and new array:', removal(digits))

# Print 2D array duplicate(s) found --------------------------------------------------------------------------------------------------------

def printing(arr: list[list[int]]) -> list[list[int]]:
    seen = set()
    result = []
    for row in arr:
        new_array = []
        for num in row:
            if num not in seen:
                seen.add(num)
            else:
                new_array.append(num)
        if new_array:
            result.extend(new_array)
    return result
print('Printing 2D duplicate using set() and new array:', printing(digits))
# for i in printing(digits):
#     for j in i:
#         print(j, end=', ')
print(end=None)        
    








