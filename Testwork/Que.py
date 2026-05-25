import re as rex
import heapq
from collections import deque, Counter
from itertools import permutations

# python -u "C:\Users\JosephET\Documents\VS Code\Workspace\Testwork\Que.py"

'''
# My Sorting engine
## Returns the input type NB: *arryRes* changes (int and str) input result to a list
# int with zero(s) to be sorted in ascending order would lose zero(s) (e.g 602436 -> 24366) 
# except the use of *arryRes* parameter as *True* to convert result to a list (e.g 602436 -> [0, 2, 4, 3, 6, 6])
# or gain the zero(s) by using reverse=True (e.g 602436 -> 664320)

def allSorted(li, reverse: bool = False, arryRes: bool = False):
    if type(li) == list:
        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                if reverse:
                    if li[i] < li[j]:
                        temp = li[i]
                        li[i] = li[j]
                        li[j] = temp
                else:
                    if li[i] > li[j]:
                        temp = li[i]
                        li[i] = li[j]
                        li[j] = temp

    if type(li) == str:
        res = [x for x in li]
        for i in range(len(res)):
            for j in range(i + 1, len(res)):
                if reverse:
                    if res[i] < res[j]:
                        temp = res[i]
                        res[i] = res[j]
                        res[j] = temp
                else:
                    if res[i] > res[j]:
                        temp = res[i]
                        res[i] = res[j]
                        res[j] = temp
        if arryRes:
            return res
        res = (''.join(res))
        li = res

    if type(li) == int:
        res = [x for x in str(li)]
        for i in range(len(res)):
            for j in range(i + 1, len(res)):
                if reverse:
                    if res[i] < res[j]:
                        temp = res[i]
                        res[i] = res[j]
                        res[j] = temp
                else:
                    if res[i] > res[j]:
                        temp = res[i]
                        res[i] = res[j]
                        res[j] = temp
        if arryRes:
            return [x for x in res]
        res = (''.join(res))
        li = int(res)

    # Not tested yet!
    # if type(li) == None:
    #     # return TypeError("ERROR: \'None\' not iterable")
    #     return TypeError("ERROR: 'None' not iterable")
    # return li if type(li) != None else None
    return li

sL = [7, 2, 8, 6, 4]
# sL = ["z", "x", "a", "o", "b"]
# sL = "zxaob"
# sL = 412769
print(allSorted(sL))

------------------------------------------------------------------------------
# Insert engine (supports negative indexing)
# nn = [6, 4, 3, 5, 1, 8, 2, 9]
# k = -10

# print(nn)
# def inserted(nums: list[int], index: int, val: int) -> list[int]:

#     # l = len(nums) + 1
#     # err = l + (-l * 2) + (-1)

#     l = len(nums)
#     err = l + (-l * 2) + (-2)
    
#     if index <= err or index >= len(nums) + 1:
#         return IndexError("ERROR: Index out of range!")
#     if index < 0:
#         index = (len(nums) + 1) + index
#     nums[:] = nums[:index] + [val] + nums[index:]
#     return nums
# print(inserted(nn, k, -1))

------------------------------------------------------------------------------
# pop engine (supports negative indexing)
# nn = [4, 3, 5, 1, 8]
# k = 5

# print(nn)
# def popped(nums: list[int], index: int) -> list[int]:

#     l = len(nums)
#     err = l + (-l * 2) + (-1)
    
#     if index <= err or index >= len(nums):
#         return IndexError("ERROR: Index out of range!")
#     if index < 0:
#         index = len(nums) + index
#     nums[:] = nums[:index] + nums[index + 1:]
#     return nums
# print(pop(nn, k))

------------------------------------------------------------------------------
# Removes an element in an array (count -> how many occurrence(s) of the value to remove)
see = [4, 1, 0, 8, 2, 1, 2, 5, 0]
print(see)
def removed(nums: list[int], value: int, count: int = 1) -> list[int]:
    if value not in nums:
        return ValueError("ValueError: Value or element not in list!")
    if nums.count(value) < count:
        return IndexError("IndexError: Count out of range!")
    counter = 0
    for i in range(len(nums)):
        if nums[i] == value:
            nums[:] = nums[:i] + nums[i + 1:]
            counter += 1
            if counter == count:
                break
    return nums
print(removed(see, 1))

-----------------------------------------------------------------------------------------------------------------------------------
# Replaces an element (old) with a new (new) element (count -> how many occurrence(s) of the old or current to be replaced)
# see = [4, 1, 0, 8, 2, 1, 2, 5, 0]
print(see)
def replaced(nums: list[int] | list[str], old: int | str, new: int | str, count: int = 1) -> list[int]:
    if old not in nums:
        return ValueError("ValueError: old parameter or element not in list!")
    if nums.count(old) < count:
        return IndexError("IndexError: Count out of range!")
    counter = 0
    for i in range(len(nums)):
        if nums[i] == old:
            nums[i] = new
            counter += 1
            if counter == count:
                break
    return nums
print(replaced(see, 1, 44, 2))

-----------------------------------------------------------------------------------------------------------------------------------
# Split string value into list

uni = "Tosin, Joseph, Emmanuel"
def splitted(string: str, target: str) -> list:
    str_store = []
    res = []
    for i, char in enumerate(string):
        if char == target:
            joined = (''.join(str_store))
            res.append(joined)
            str_store.clear()
        elif char != ' ':
            str_store.append(char)
        if i == len(string) - 1:
            if len(res) < 1:
                return -1
            joined = (''.join(str_store))
            res.append(joined)
    return res
un = splitted(uni, ",")
print(un)

'''
0#
'''
controller = rex.compile(r"(\d)\1")
controllerPlus = rex.compile(r"(\d)\1\1")

testStr = ["444passw88", "p55assw444", "passw44", "passw11"]

for i in range(len(testStr)):
    if controllerPlus.search(testStr[i]):
        idx = controllerPlus.search(testStr[i]).regs[1][0]
        m = int(testStr[i][idx]) * 3
        if len(str(m)) > 1:
            testStr[i] = testStr[i].replace(testStr[i][idx], str(m), 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 2], '', 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 2], '', 1)
        elif len(str(m)) == 1:
            testStr[i] = testStr[i].replace(testStr[i][idx], str(m), 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 1], '', 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 1], '', 1)

    if controller.search(testStr[i]):
        idx = controller.search(testStr[i]).regs[1][0]
        m = int(testStr[i][idx]) * 2
        if len(str(m)) == 1:
            testStr[i] = testStr[i].replace(testStr[i][idx], str(m), 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 1], '', 1)
        elif len(str(m)) > 1:
            testStr[i] = testStr[i].replace(testStr[i][idx], str(m), 1)
            testStr[i] = testStr[i].replace(testStr[i][idx + 2], '', 1)

print(testStr)
# More Efficient way

# string = "Jaize7888" # Jaize31
# string = "121212Jaize" # 9Jaize
# string = "121Jaize457Tosin405" # 4Jaize16Tosin9
# string = "121212Jaize45" # 9Jaize9
# string = "121212Jaize444" # 9Jaize12
string = ["passw88", "47passw444", "passw44", "passw11"]


def dupString(s: str | list[str]) -> str:
    str_store = []
    store = []
    cur_dig = 0
    if type(s) == list:
        l = 0
        while l < len(s):
            for i, char in enumerate(s[l]):
                if char.isdigit():
                    cur_dig += int(char)
                    if len(str_store) > 0:
                        store.append((''.join(str_store)))
                        str_store.clear()
                if (not char.isdigit()):
                    str_store.append(char)
                    if cur_dig > 0:
                        store.append(cur_dig)
                        cur_dig = 0
                if i == len(s[l]) - 1:
                    if len(str_store) > 0:
                        store.append((''.join(str_store)))
                    elif cur_dig > 0:
                        store.append(cur_dig)
            s[l] = (''.join(str(x) for x in store))
            store.clear()
            str_store.clear()
            cur_dig = 0
            l += 1
        return s
    else: 
        for i, char in enumerate(s):
            if char.isdigit():
                cur_dig += int(char)
                if len(str_store) > 0:
                    store.append((''.join(str_store)))
                    str_store.clear()
            if (not char.isdigit()):
                str_store.append(char)
                if cur_dig > 0:
                    store.append(cur_dig)
                    cur_dig = 0
            if i == len(s) - 1:
                if len(str_store) > 0:
                    store.append((''.join(str_store)))
                elif cur_dig > 0:
                    store.append(cur_dig)
        return (''.join(str(x) for x in store))

dupstr = dupString(string)
print(dupstr)

'''

# 1.
'''
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def tester(no: list[int]):
    max_sum = float('-inf')
    current_sum = 0
    for i in no:
        current_sum = max(i, current_sum + i)
        max_sum = max(max_sum, current_sum)
        # Method 2
        # if current_sum > max_sum:
        #     max_sum = current_sum
    return max_sum

print(tester(nums))
'''

# 2.
'''
front = list((5, 2, 1, 5, 8, 4))
target = 10

archive = set()
pair = []

for i in front:
    com = target - i
    if com in archive:
        pair.append((com, i))
    archive.add(i)


for i in pair:
    for j in i:
        if j == 8:
            print(j, end='')
            continue
        print(j, end=', ')
'''

# 3.
'''

first = [7, 8, 9, 1, 2]
second = [4, 3, 6]

print(*first, sep=', ')
print(*second, sep=', ')

all = []
all.extend(first)
all.extend(second)
all.sort()

xx = []
yy = []

for i in range(len(all)):
    if i <= len(first) - 1: 
        xx.append(all[i])
    else:
        yy.append(all[i])


print(*xx, sep=', ')
print(*yy, sep=', ')
'''

#4
'''
first = 'Jaize'
second = [1, 4, 2, 3, 8, 5]
third = ["T", "y", "c", "o", "o", "n"]
fourth = ["Emmanuel", "jaize", "Tosin"]
seeAllthem = [first, second, third, fourth]

def ultimateProx(allOf: list) -> list[int, str]:
    res = []
    for i in allOf:
        if type(i) == list:
            if type(i[0]) == str:
                if len(i[0]) == 1:
                    # all = (''.join(i))
                    all = (''.join(x for x in i))
                    res.append(all)
                    continue
                else:
                    res.extend(i)
                    continue
            else:
                res.extend(i)
                continue
        res.append(i)
    return res
         
today = ultimateProx(seeAllthem)
print(*today, sep=", ")

final = []

for i in fourth:
    if i[0] == i[0].lower():
        work = i[0].upper() + i[1:len(i)].lower()
        final.append(work)


'''

#5
'''
# Explanation
# times = [['source_node / starting pos', 'edge / destination', 'distance']]
# n = "amount_of_edge(s)"
# k = "source_node"
# graph = [['source_node']]
# graph = [[('edge / destination', 'distance')]]

# graph = [[], [], [(1, 1), (3, 1)], [(4, 1)], []]

# times = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]] # 3
# n = 5
# k = 2

# times = [[1, 2, 1]] # 1
# n = 2
# k = 1

# times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]] # 2
# n = 3
# k = 1

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]] # 2
n = 4
k = 2

class Solution:
    def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        # Alternative method (might not be efficient though)
        # max_res = 0
        # d = []
        # for a, b, c in times:
        #   if b < k:
        #         s = k - b
        #     else:
        #         s = b - k
        # You can just return s without the two-line additional code below
        #    d.append(s)
        # max_res = max(d)
        # return max_res    

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        pq = [(k, 0)]
        while pq:
            u, d = heapq.heappop(pq)
            if d > distance[u]:
                continue
            for v, w in graph[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(pq, (v, distance[v]))
        max_distance = max(distance[1:])
        return max_distance if max_distance != float('inf') else -1  


obj = Solution
myResult = obj.networkDelayTime(times=times, n=n, k=k)

print(myResult)
'''

#6
'''

class Testing:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]

numbers = [7, 7, 7, 7, 8, 3]
k = 4

objTest = Testing(k, numbers)

print(f"For 2 = {objTest.add(2)}")
print(f"For 10 = {objTest.add(10)}")
print(f"For 9 = {objTest.add(9)}")
print(f"For 9 = {objTest.add(9)}")


'''

#7
'''

# bits = [1, 1, 1, 0] # false
# bits = [1, 1, 1, 1, 1] # 2 2 1 true
# bits = [1, 1, 0, 1, 0, 0, 1, 1, 0] # true
# bits = [1, 0, 0] # true
bits = [1, 0, 0, 0] # true

def isOneBit(bits: list[int]) -> bool:
    # Not proven to be efficient
    # source = [1, 2, 3, 5, 6]
    # seen = False
    # for i in source:
    #     if len(bits) == i:
    #         seen = True
    # return seen
    i = 0
    while i < len(bits) - 1:
        i += bits[i] + 1
    return i == len(bits) - 1

print(isOneBit(bits))

'''

#8
'''
from itertools import permutations

# arr = [1, 4, 3, 2] # 23:41
# arr = [1, 2, 3, 0] # 23:10
# arr = [2, 3, 4, 4] # 23:44
# arr = [0, 0, 0, 0] # 00:00
# arr = [0, 0, 1, 0] # 10:00
arr = [5, 5, 1, 5] # 15:55

def largestTime(time: list[int]) -> str:
    max_time = -1
    for h1, h2, m1, m2 in permutations(time):
        hours = h1 * 10 + h2
        minutes = m1 * 10 + m2
        
        if hours < 24 and minutes < 60:
            max_time = max(max_time, (hours * 60 + minutes))

    
    if max_time == -1:
        return ""
    else:
        hours, minutes = divmod(max_time, 60)
        return f"{hours:02d}:{minutes:02d}"
       

res = largestTime(arr)
print(res)

'''

#9
'''
s = ["h", "e", "l", "l", "o"]

class Solution:
    def __init__(self, s: list[int]):
        self.s = s
    def display(self) -> str:
        low, high = 0, len(self.s) - 1

        while low < high:
            self.s[low], self.s[high] = self.s[high], self.s[low]
            low += 1
            high -= 1
        print(f"{self.s}")
        # return self.s
'''

#10
'''
# mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]  # 24
# height: [[0, 1, 1, 0], [0, 2, 2, 1], [1, 3, 3, 0]]
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]] # 13
# height: [[1, 0, 1], [2, 1, 0], [3, 2, 0]]

class Solution:
    def __init__(self, mat: list[int]):
        self.mat = mat
    def display(self) -> None:
        m, n = len(self.mat), len(self.mat[0])
        # height = [[0] * len(x) for x in self.mat]
        height = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.mat[i][j] == 1:
                    height[i][j] = height[i - 1][j] + 1 if i > 0 else 1

        res = 0
        for i in range(m):
            for j in range(n):
                if self.mat[i][j] == 1:
                    min_height = height[i][j]
                    for k in range(j, -1, -1):
                        if self.mat[i][k] == 0:
                            break
                        min_height = min(min_height, height[i][k])
                        res += min_height
        return res
        
    
    
obj = Solution(mat)
res = obj.display()
'''

#11
'''
# s = "LPLPLP" # True
# s = "LALL" # True
# s = "LAAL" # False
# s = "LLLL" # False
# s = "LALPLPLA" # False
s = "LLALLPLLPLL" # True
# s = "PLLLA" # False

def working(array: str, k: int = 0) -> bool:
    controll = rex.compile(r"(L)\1\1")
    if controll.search(array) or array.count("A") >= 2:
        return False
    return True
work = working(s)
print(work)


class Solved:
    # @staticmethod
    def checkRecord(s: str) -> bool:
        aes = s.count('A')
        if aes >= 2:
            return False
        
        for i in range(len(s) - 2):
            if s[i] == 'L' and s[i + 1] == 'L' and s[i + 3] == 'L':
                return False
        return True

sol = Solved()
sol = sol.checkRecord(s)
print(sol)
'''

#12
'''
# put = round(float(input("Input a number to make a spiral display: ")))
# n = put
n = 5

def spiral(n: int) -> list[int]:
    matrix = [[0] * n for _ in range(n)]
    m = (n * n) + 1
    #Right, Down, Left, Up 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    row, col = 0, 0
    for i in range(1, m):
        matrix[row][col] = i
        # Next element replacement
        nxt_row, nxt_col = row + directions[dir_idx][0], col + directions[dir_idx][1]

        # Confirm movement before pushing through / proceeding
        if 0 <= nxt_row < n and 0 <= nxt_col < n and matrix[nxt_row][nxt_col] == 0:
            row, col = nxt_row, nxt_col
        else:
            # Change position or direction
            dir_idx = (dir_idx + 1) % len(directions) # 4
            row, col = row + directions[dir_idx][0], col + directions[dir_idx][1]
    return matrix

obj = spiral(n)
for i in obj:
    print(i)

'''

#13
'''
from collections import deque

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]] # 4
# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]] # -1

class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        minutes = 0
        # Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                   queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = (x + dx), (y + dy)

                    if (0 <= nx < m) and (0 <= ny < n) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
        return minutes if fresh_count == 0 else -1


obj = Solution()
res = obj.orangesRotting(grid)
print(res)
'''

#14
'''
title = "AAB" # 8
# title = "AAABBC" # 188

def Perm(n: str) -> int:
    m = len(n)
    mSet = set()
    while m > 0:
        for i in permutations(n, m):
            mSet.add(i)
        m -= 1    
    return len(mSet)

perm = Perm(title)
print(perm)

sss = "RLRRLLRLRL" # 4
# sss = "RLRRRLLRLL" # 2
# sss = "LLLLRRRR" # 1
# sss = "LRLRLRRRLLLRLRL" # 6

def balancedStrSplit(s: str) -> int:
    bal = 0
    count = 0
    for i in s:
        if i == "R":
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            count += 1
    return count
fin = balancedStrSplit(sss)
# print(fin)

'''

#15
'''
# paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
# no = 4
# paths = [[1, 2], [2, 3], [3, 1]]
# no = 3
paths = [[1, 2], [3, 4]]
no = 4

def gardenNoAdj(n: int, paths: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    colors = [0] * n

    for x, y in paths:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    
    for i in range(n):
        used_colors = set(colors[x] for x in graph[i])
        for color in range(1, 5):
            if color not in used_colors:
                colors[i] = color
                break

    return colors

rr = gardenNoAdj(no, paths)
print(rr)
'''

#16
'''
words = ["cool"]
# words = ["bella", "label", "roller"]
# words = ["cool", "lock", "cook"]
# words = ["acabcddd", "bcbdbcbd", "baddbadb", "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]
# words = ["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]

def commonChar(words: list[str]) -> list[str]:
    # My code
    # if len(words) == 1:
    #     one = []
    #     for i in range(len(words[0])):
    #         one.append(words[0][i])
    #     return one
    # graph = [x for x in words[:-1]]
    # res = []
    # for i in words[-1]:
    #     last = len(graph) - 1
    #     temp = []
    #     while last > -1:
    #         if graph[last].find(i) != -1:
    #             temp.append(i)
    #             if temp.count(i) == len(words) - 1:
    #                 res.append(i)
    #             graph[last] = graph[last].replace(i, '', 1)
    #         last -= 1
    # return res

    # Main code (Most efficient)
    count = Counter(words[0])
    for i in words[1:]:
        # Only matching character(s) will be left
        count = count & Counter(i)
    return list(count.elements())

    
strs = ["flower", "flow", "flight"] # "fl"
# strs = ["dog", "racecar", "car"] # ""
# strs = ["hello", "hello world", "hello there"] # "hello"
# strs = ["apple", "apply", "appliance"] # "appl"
# strs = ["", "hello", "world"] # ""
# strs = ["a", "a", "a"] # "a"
# strs = ["abc", "abcd", "abcde"] # "abc"
# strs = ["xyz", "abc", "def"] # ""

# My code
def commonPrefix(string: list[int]) -> str:

    count = Counter(string[0])
    for i in string:
        count = count & Counter(i)
    return (''.join(list(count.elements())))
print(commonPrefix(strs))

def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len)
    # print(shortest_str[:3])

    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str

res = longestCommonPrefix(strs)
# print(res)



# More on counter
count = Counter({'z':8, 'p':5})
# or
count = Counter(z=8, p=5)
t = "acabcddd"
count = Counter(t)
sorted(count) -> ['a', 'b', 'c', 'd']
sorted(count.elements()) -> ['a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']
count.update("zzxqgh") # -> acabcdddzzxqgh
t = [7, 4, 1]
sum(t) -> 12
count = Counter(t)



res = commonChar(words)
print(res)
'''

#17
'''
s = "defdefdefabcabc" # True
goal = "defdefabcabcdef"

# s = "abcde" # True
# goal = "cdeab"

# s = "abcde" # False
# goal = "abced"

def rotateString(s: str, goal: str) -> bool:
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False


rr = rotateString(s, goal)
# print(rr)


# nums = [3, 2, 1, 7, 2, 1] # []
# nums = [3, 4, 1, 7, 2, 1, 1] # [1]
# nums = [2, 3, 3] # [3]
# nums = [2, 2] # [2]
# nums = [1, 2] # [1, 2]
# nums = [1] # [1]
# nums = [1, 2, 3] # []
# nums = [-1,-1,-2,-2] # [-1, -2]
# nums = [1, 2, 1, 2, 2, 3, 3, 1] # [1, 2]
nums = [11, 7, 1, 8, 5, 7, 12, 7] # [7]

# Greater than one-third of its length
def majorityElement(nums: list[int]) -> list[int]:
    res = []
    # done, remain = divmod(len(nums), 3)
    # Which ele. that appeared more than the len of the list // 3 ( > one-third of its length)
    done = len(nums) // 3

    count = Counter(nums)
    
    for x, y in list(count.items()):
        if y > done:
            res.append(x)
    return res

cou = majorityElement(nums)
print(cou)


# Challenge mode (2 or more)
# My code
nums = [4, 3, 2, 0, 8, 2, 3, 1, 0] # [0, 2, 3]
# nums = [4, 3, 2, 7, 8, 2, 3, 1] # [2, 3]
# nums = [1, 1, 2] # [1]
# nums = [1] # []

def product(nums: list[int]) -> list[int]:
    # Shortest implementation that meets the condition 

    # In order to get an ascending array result
    # nums.sort()
    # output = []

    # for i in nums:
    #     if nums.count(i) >= 2:
    #         if i not in output:
    #             output.append(i)

    # Longest, tricky implementation 
    
    # In order to get an ascending array result
    nums.sort()
    count1 = -1
    count2 = 0
    count3 = 0
    # Not necessary
    count4 = 0
    count5 = 0
    isOccupied: bool = False
    # output = []

    for i in nums:
        if nums.count(i) >= 2:
            if count1 == -1 and isOccupied == False:
                count1 = i
                isOccupied = True
            elif count2 == 0 and i != count1:
                count2 = i
            elif count3 == 0 and i != count1 and i != count2:
                count3 = i
            elif count4 == 0 and i != count1 and i != count2 and i != count3:
                count4 = i
            elif count5 == 0 and i != count1 and i != count2 and i != count3 and i != count4:
                count5 = i

    if count1 != -1 and isOccupied == True:
        output.append(count1)
    if count2 != 0:
        output.append(count2)
    if count3 != 0:
        output.append(count3)
    if count1 == 0 and count2 == 0 and count3 == 0 and count4 == 0 and count5 == 0:
        output = []
    if count4 != 0:
        output.append(count4)
    if count5 != 0:
        output.append(count5)      

    

    
    return output
r = product(nums)
print(r)


# My code (2 or more)
def product(nums: list[int]) -> list[int]:
    nums.sort()
    output = []
    store = set()
    for i in nums:
        if nums.count(i) >= 2:
            store.add(i)
    output.extend(list(store))
    
    return output
    # or
    # res = []
    # counter = Counter(nums)
    # for a, b in list(counter.items()):
    #     if b >= 2:
    #         res.append(a)
    # res.sort()
    # return res
r = product(nums)
print(r)



'''

#18
'''
# rotate = [1, 2, 3, 4, 5, 6, 7]
rotate = [-1, -100, 3, 99, 0]
r = 3

def rotateList(rot: list[int], r: int) -> list[int]:
    # Or
    # r %= len(rot)
    # return rot[:] = rot[-r:] + rot[:-r]
    for i in range(r):
        rot[:] = rot[-1:] + rot[:-1]
    return rot
print(rotateList(rotate, r))


Product = [1, 2, 3, 4] # [24, 12, 8, 6]

def productList(prod: list[int]) -> list[int]:
    res = []
    for i in range(len(prod)):
        m = 0
        temp = 1
        while m <= len(prod) - 1:
            if prod[m] == prod[i]:
                m += 1
                continue
            else:
                temp *= prod[m]
            m += 1
        res.append(temp)
    return res
print(productList(Product))

'''

#19
'''
# nums = [] # []
# nums = [0, 1, 1] # []
# nums = [1] # []
# nums = [1, 2] # []

# nums = [-1, 0, 1, 2, -1, -4] # [[-1, 0, 1], [-1, -1, 2]]
# nums = [-5, -3, 0, 1, 3, 6] #[[-3, 0, 3]]
# nums = [-2, 0, 3, 2, -1, -2] # [[-2, -1, 3], [-2, 0, 2]]
nums = [-1, 0, 3, -2, 4, -4] # [[-2, -1, 3], [-4, 0, 4]]
tri = 3

# My code
def triplets(nums: list[int], tri: int) -> list[int]:
    res = set()
    for i, j, k in permutations(nums, tri):
        if i + j + k == 0:
            res.add((i, j, k))

    strain = set()
    for i, j, k in list(res):
        all = sorted([i, j, k])
        strain.add((all[0], all[1], all[2]))

    return [[y for y in x] for x in strain]
# print(triplets(nums, tri))


# More Efficient (Mine)
def triplets(nums: list[int], tri: int) -> list[int]:
    res = set()
    for i, j, k in permutations(nums, tri):
        if i + j + k == 0:
            all = sorted([i, j, k])
            res.add((all[0], all[1], all[2]))

            # For list variable
            # if [all[0], all[1], all[2]] not in [[y for y in x] for x in store]:
            #     store.append((all[0], all[1], all[2]))

    return [[y for y in x] for x in res]

# AI
def threeSum(nums: list[int]) -> list[int]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res
print(threeSum(nums))

'''

#20
'''
# close = [-1, 2, 1, -4] # [2]
# t = 1
# close = [0, 0, 0] # [0]
# t = 1
# close = [0, 1, 2] # [3]
# t = 4
# t = 3
# close = [12, 34, 56, 78, 90] # [146]
# t = 150
# close = [1, 1, 1] # [3]
# t = 2
close = [1, 2, 8, 16, 32, 64, 128, 256] # [82]
t = 82
# close = [1, 2, 3, 4, 5] # [8]
# t = 8
# close = [-5, -3, 0, 1, 3, 6] # [0]
# t = 0
# close = [] # []
# t = 0

# My code
def solve(paths: list[int], target: int) -> list[int]:
    if len(paths) == 0: return []
    store = set()
    for x, y, z in permutations(paths, 3):
        Sum = x + y + z
        store.add(Sum)
        if Sum == target: return Sum
    
    if len(paths) > 0:
        left = target - 1
        right = target + 1
        while True:
            if left in store: return left
            elif right in store: return right
            left -= 1
            right += 1    
sol = solve(close, t)
print(sol)


# AI
def closestTarg(nums: list[int], target: int) -> int:
    nums.sort()
    closest_num = float('inf')

    for i in range(len(nums) - 1):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_num - target):
                closest_num = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
    return closest_num

print(closestTarg(close, t))

'''

#21
'''
string = ["eat", "tea", "tan", "ate", "nat", "bat"] # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] Any order
# string = [""] # [[""]]
# string = ["a"] # [["a"]]
def grpAnagrams(string: list[str]) -> list[list[str]]:
    temp = set()
    res = []
    for i in string:
        for j in permutations(i, len(i)):
            joined = (''.join(j))
            if joined in string and joined not in [y for x in res for y in x]:
                temp.add(joined)
        if len(temp) > 0:
            # res.append([x for x in temp])
            res.append(list(temp))
        temp.clear()
    # del string
    # del joined
    # del temp
    return res
# print(grpAnagrams(string))


#        0  1  2  3  4  5  6  7  8
height= [1, 8, 6, 2, 5, 4, 8, 3, 7] # 49 (n = 9, len = 8)
height= [1, 1] # 1
height= [4, 2, 7, 5, 6] # 16 (n = 5, len = 4)

def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # two walls, the water can't go beyond the minimum or smaller wall (otherwise the water will spill over)
        h = min(height[left], height[right])
        # width
        w = right - left
        # area-of-water formula
        area = h * w

        max_area = max(max_area, area)

        # Increament the smaller line or wall because it has the possibility of an increased area value
        if height[left] < height[right]: left += 1
        else: right -= 1

    return max_area
r = maxArea(height)
# print(r)

'''

#22
'''
# perms = [1, 2, 3] # [1, 3, 2]
# perms = [3, 2, 1] # [1, 2, 3]
# perms = [1, 1, 5] # [1, 5, 1]
# perms = [1, 4, 5] # [1, 5, 4]

perms = [4, 2, 3, 1] # [4, 3, 1, 2]
# perms = [2, 3, 1] # [3, 1, 2]
# perms = [2, 3, 1, 2] # [2, 3, 2, 1]
# perms = [2, 3, 3, 2] # [3, 2, 2, 3]


# My code
def nxtPerm(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    store = set()
    for x in permutations(nums, len(nums)):
        joiner = (''.join(str(v) for v in x))
        store.add(joiner)
    
    store = sorted(store)
    for i in store:
        main_nums = (''.join(str(v) for v in nums))
        if int(i) > int(main_nums):
            return [int(x) for x in list(i)]
    return sorted_nums
print(nxtPerm(perms))



def nxtPerm(nums: list[int]) -> list[int]:

    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverse(nums, start):
        left, right = start, len(nums) - 1

        while left < right:
            swap(nums, left, right)
            left += 1
            right -= 1

    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)

    reverse(nums, i + 1)
    # return nums

r = nxtPerm(perms)
# print(nxtPerm(perms))

'''

#23
'''
# nums = [1, 2, 3, 4, 5] # 12
# k = 3
# m = 3

# nums = [1, 1, 1, 1, 1] # 0
# k = 4
# m = 2

# nums = [2, 4, 3, 4, 5, 3, 2, 1] # 16
# k = 4
# m = 3

nums = [1, 2, 1, 2, 1, 2, 1] # 6
k = 4
m = 2

# nums = [1, 5, 4, 0, 3, 2] # 14
# k = 4
# m = 4

def almostUnique(nums: list[int], k: int, m: int) -> int:
    # Sort for the duplicate (variable <store>: list) to get the highest number at the end of its container ([-1], as the last element, value or item)
    nums.sort()
    max_sum = 0
    store = []


    for i in nums: 
        if nums.count(i) >= 2 and i not in store: store.append(i)


    for temp in permutations(nums, k):
        if list(temp)[-1] not in list(temp)[:m - 1]:
            if len(store) > 0:
                if list(temp).count(store[-1]) <= 2:
                    s = sum(temp)
                    max_sum = max(max_sum, s)
            else:
                s = sum(temp)
                max_sum = max(max_sum, s)
    return max_sum

res = almostUnique(nums, k, m)
print(res)


# uni = [1, 1, 4, 4, 4, 3, 1, 1, 4, 3] # -1
# quanti = 4
# uni = [1, 1, 4, 4, 2, 4, 3, 1, 1, 4, 3]
# quanti = 4
uni = [1, 1, 4, 4, 2, 4, 3, 0, 1, 4, 3]
quanti = 5
def unique(nums: list[int], many: int) -> list[int]:
    for i in permutations(nums, many):
        count, step = 0, 0
        while step < len(i):
            if list(i).count(i[step]) == 1: count += 1
            step += 1
        if count == many: return list(i)
    return -1
un = unique(uni, quanti)
print(un)

'''

#24
'''

# prod_list = [5, 0, -5] # 5
# prod_list = [0, 2] # 2
prod_list = [-1, -2, -3, -4] # 24
# prod_list = [2, 3, -2, 4] # 6
# prod_list = [-2, 0, -1] # 0

def maxProd(nums: list[int]) -> int:
    def prod(input: list[int]) -> int:
        temp = 1
        for i in input:
            temp *= i
        return temp
    
    r = 1
    max_prod = 0
    while r <= len(nums):
        core = (len(nums) + 1) - r
        for i in range(core):
            p = prod(nums[i : i + r])
            max_prod = max(max_prod, p)
        r += 1
    return max_prod
# pp = maxProd(prod_list)
# print(pp)



# prod_max = [10, 20, 30] # 0
# k = 10
# prod_max = [5, 5, 5] # 3
# k = 25
prod_max = [1, 1, 1] # 6
k = 2
# prod_max = [10, 5, 2, 6] # 8
# k = 100
# prod_max = [1, 2, 3] # 0
# k = 0

def maxSubProd(nums: list[int], k: int) -> int:
    def prod(input: list[int]) -> int:
        temp = 1
        for i in input:
            temp *= i
        return temp
    
    track = 1
    # output = []
    output = 0
    while track <= len(nums):
        core = (len(nums) + 1) - track
        for i in range(core):
            p = prod(nums[i : i + track])
            if p < k:
                # output.append(p)
                output += 1
        track += 1
    # return len(output)
    return output
mm = maxSubProd(prod_max, k)
print(mm)
'''

#25
'''
# con = [100, 0, 200, 1, 2, 3] # 4
# con = [1] # 1
# con = [1, 2] # 2
# con = [1, 0, 2, 0, 8, 3, 7, 6, 4, 5] # [0 - 8] -> 9
con = [1, 0, 2, 0, 8, 100, 7, 6, 10, 5] # [5 - 8] -> 4

def longestConsecutive(nums: list[int]) -> int:
    temp = set()
    collect = []
    m = len(nums)
    
    nums.sort()
    
    if m == 1: return 1

    for i in range(m):
        if i + 1 <= m - 1:
            if nums[i + 1] - nums[i] == 1:
                temp.add(nums[i])
                temp.add(nums[i + 1])
            # else:
                # if len(temp) > 0:
            elif len(temp) > 0:
                collect.append(list(temp))
                temp.clear()
    return len(max(collect, key=len)) if len(temp) == 0 else len(temp)
    # To display the longest list itself but *collect* must not be empty
    # return sorted(max(collect)) if len(temp) == 0 else list(temp)
# print(longestConsecutive(con))

# clone = [[2, 4], [1, 3], [2, 4], [1, 3]]
clone = [[2, 3, 4], [1, 3], [1, 2, 4], [1, 2, 3], [0]]
# clone = [[2, 3, 4], [1, 3], [1, 2, 4], [1, 2, 3], [0], 5]
# clone = [[2], [1]]
# clone = [[]]
# clone = [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]

def cloneGraph(nums: list[list[int]]) -> list[list[int]]:
    m = len(nums)
    graph = [[] for _ in range(m)]

    for i in range(m):
        graph[i] = nums[i]
    return graph
print(cloneGraph(clone))

'''

#26
'''
# new_guy = ["a", "a", "b", "b", "c", "c", "c"] # 6
# new_guy = ["a"] # 1
# new_guy = ["a", "a", "a", "a", "b", "b", "b", "b"] # 4
# new_guy = ["a", "b", "c", "d", "e", "f"] # 6
# new_guy = ["a", "a", "a", "b", "b", "c", "c", "c", "c"] # 6
new_guy = ["a", "a", "b", "c", "c", "c", "c"] # 5

def charLen(chars: list[str]) -> int:
    
    if len(chars) == 1:
        return 1

    counter = Counter(chars)
    temp = []

    for c, i in list(counter.items()):
        if i > 1:
            temp.append(c)
            temp.append(str(i))
        else:
            temp.append(c)
    chars[:] = temp
    return len(chars)

cur = charLen(new_guy)
print(cur)

# nums = [2, 3, 1, 1, 4] # 2
# nums = [2, 3, 0, 1, 4] # 2
# nums = [1, 1, 1, 1, 1] # 4
nums = [1, 2, 3] # 2

def jump(nums: list[int]) -> int:
    farthest = 0
    jump = 0
    cur_jump = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, nums[i] + i)

        if i == cur_jump:
            jump += 1
            cur_jump = farthest
    return jump    
# print(jump(nums))


# rev = "the sky is blue" # blue is sky the
# rev = " hello world! " # world! hello
rev = "a good  example" # example good a
# rev = "Emmanuel Tosin Joseph" # Joseph Tosin Emmanuel
def revString(rev: str) -> str:
    rev = rev.strip(' ')
    rev = rev.split(' ')
   
    idx = len(rev) - 1
    temp = []

    for i in range(idx, -1, -1):
        if rev[i] == "":
            continue
        temp.append(rev[i])
        if i > 0:
            temp.append(" ")
    return (''.join(temp))
    
rrr = revString(rev)
print(rrr)

'''

#27
'''
# version1 = "0.1" 
# version2 = "1.1.5.0" # -1
# version1 = "0.1" 
# version2 = "1.1" # -1
# version1 = "1.0.1"
# version2 = "1" # 1
# version1 = "7.5.2.4" 
# version2 = "7.5.3" # -1
version1 = "7.5.3" 
version2 = "7.5.3" # 0

def verison(ver1: str, ver2: str) -> int:
    # ver1 = ver1.split('.')
    # ver2 = ver2.split('.')
    # length = len(max(ver1, ver2, key=len))

    # filling method 1
    # temp_1 = [[] for _ in range(length)]
    # temp_2 = [[] for _ in range(length)]

    # for core in range(length):
    #     # filling method 1
    #     if core <= len(ver1) - 1:
    #         temp_1[core] = ver1[core]
    #     else:
    #         if core >= len(ver1):
    #             temp_1[core] = 0
            
    #     if core <= len(ver2) - 1:
    #         temp_2[core] = ver2[core]
    #     else:
    #         if core >= len(ver2):
    #             temp_2[core] = 0
    #     # filling method 2
    #     # temp_1 = ver1[core] if core < len(ver1) else 0
    #     # temp_2 = ver2[core] if core < len(ver2) else 0
        
    #     if int(temp_1[core]) > int(temp_2[core]):
    #         return 1
    #     elif int(temp_1[core]) < int(temp_2[core]):
    #         return -1
    # return 0
    
    # AI deep-search technique
    ver_1 = ver1.split('.')
    ver_2 = ver2.split('.')

    for v1, v2 in zip_longest(ver_1, ver_2, fillvalue="0"):
        if int(v1) > int(v2):
            return 1
        elif int(v1) < int(v2):
            return -1
    return 0
         

com_ver = verison(version1, version2)
print(com_ver)



# inp_1 = "cbaebabacd"
# inp_2 = "abc" # [6, 0] Any order
# inp_1 = "abab"
# inp_2 = "ab" # [0, 1, 2]
# inp_1 = "ababhfcbadjab"
# inp_2 = "ab" # [0, 1, 2, 7, 11]
inp_1 = "ateteaeat"
inp_2 = "eat" # [0, 3, 6]

def anagram(s: str, p: str) -> list[int]:
    res = []
    # res = set()
    rng = len(p)
    core = len(s)

    for i in permutations(p, rng):
        compld = (''.join(i))
        for j in range(core):
            strain = s.find(compld, j, core)
            if strain != -1 and strain not in res:
                res.append(strain)
            # if strain != -1:
            #     res.add(strain)
            else:
                continue
    # return list(res)
    # return sorted(res)
    # list can be in any order
    res.sort()
    return res
ana = anagram(inp_1, inp_2)
print(ana)

'''

#28
'''
# pp = "3+2*2" # 7
# pp = "3/2" # 1
# pp = "3+5 / 2" # 5
# pp = " 3 / 2 " # 1
# pp = "1+2+3+4" # 10
# pp = "1-2+3-4" # -2
# pp = "2*3+4*5" # 26
# pp = "10/2+3*2" # 11
# pp = "100/10-5" # 5
# pp = " 5 + 5 " # 10
pp = " 10- 5+2 " # 7

def operator(s: str) -> int:
    operation = "+"
    res = []
    curr_num = 0
    for i, char in enumerate(s):
        # if char.isdigit():
        if char.isnumeric():
            curr_num = curr_num * 10 + int(char)
        if (not char.isnumeric() and not char.isspace()) or i == len(s) - 1:
            if operation == "+":
                res.append(curr_num)
            elif operation == "-":
                res.append(-curr_num)
            elif operation == "/":
                # res.append(int(res.pop() / curr_num))
                res[-1] = int(res[-1] / curr_num)
            elif operation == "*":
                # res.append(int(res.pop() * curr_num))
                res[-1] = int(res[-1] * curr_num)
            operation = char
            curr_num = 0
    return sum(res)
ope = operator(pp)
# print(ope)

'''

# To display array in range of k
# k = 2
# core = (len(nums) + 1) - k
# for i in range(core):
#     s = sum(nums[i : i + k])
#     max_sum = max(max_sum, s)

# tempo = [1, 2, 3, 4, 5]
# tempo[:] = tempo[0:-2] + tempo[:-3:-1]
# print(tempo) # [1, 2, 3, 5, 4]

# ss = [4, 2]
# ss[:] = ss + [6, 7] # [4, 2, 6, 7]
# ss[:] = ss[:] + [6, 7] # [4, 2, 6, 7]
# ss[:] = ss[:] + [ss[0], 7] # [4, 2, 4, 7]
# ss[-1] = [ss[-1], 7] # [4, [2, 7]]
# ss[-1] = ss[-1], 7 # [4, (2, 7)]


#  Working with file

# file = open('py_text.txt', 'r+')
# file = open('py_text.txt', 'a+')
# file.write("Joseph, Tosin, Emmanuel")
# file.write("\nFull-stack")
# if file.readable():
#     print(file.readlines())
# file.close()





num_String = ["+4", "-5", "1"]
diff = 1

for i in num_String:
    if i.find('e') != -1:
        me = i.find('e')
        print('Yes', i, me)
    else:
        me = i.find('e')
        print('No', i, me)




# names = ("154 545 6669")
# names = ("115 545 1119")
names = ("154 5455 669") # Got Error
# names = ("2234 57777") # 2 in 1 front and back
# names = ("23345877")



# Consecutive string numbers manipulation to sum!
# '''
print("Original Value:", names)
def work(s: str) -> str:
    names = s
    result = ""
    for num in names.split():
        for i in range(len(num)):
            if i + 3 < len(num) and num[i] == num[i + 1] and num[i] == num[i + 2] and num[i] == num[i + 3]:
                sum = int(num[i]) * 4
                if len(str(sum)) > 1:
                    num = num.replace(num[i], str(sum), 1)
                    num = num.replace(num[i + 2], "", 1)
                    num = num.replace(num[i + 2], "", 1)
                    num = num.replace(num[i + 2], "", 1)
                elif len(str(sum)) == 1:
                    num = num.replace(num[i], str(sum), 1)  
                    num = num.replace(num[i + 1], "", 1)
                    num = num.replace(num[i + 1], "", 1)
                    num = num.replace(num[i + 1], "", 1)
            elif i + 2 < len(num) and num[i] == num[i + 1] and num[i] == num[i + 2]:
                sum = int(num[i]) * 3
                if len(str(sum)) > 1:
                    num = num.replace(num[i], str(sum), 1)
                    num = num.replace(num[i + 2], "", 1)
                    num = num.replace(num[i + 2], "", 1)
                elif len(str(sum)) == 1:
                    num = num.replace(num[i], str(sum), 1)
                    num = num.replace(num[i + 1], "", 1)
                    num = num.replace(num[i + 1], "", 1)
            elif i + 1 < len(num) and num[i] == num[i + 1]:
                sum = int(num[i]) * 2
                if len(str(sum)) > 1:
                    num = num.replace(num[i], str(sum), 1)
                    num = num.replace(num[i + 2], "", 1)
                elif len(str(sum)) == 1:
                    num = num.replace(num[i], str(sum), 1)
                    num = num.replace(num[i + 1], "", 1)
        result += num + " "
    s = result
    return s

print("Result:", work(names))



bigNo = 25545236
formated = "{:,}".format(bigNo)
# formated = f"{bigNo:,}"

# print(f"{bigNo:.<11}")
print(formated)


# fi = 1985
fi = 1995
che = 2086 # Approximation of 5 does not work on even numbers
fir = round(fi, -1)
new = round(che, -2)

print(fi, '=', fir)
print(che, '=', new)


# Date format
from datetime import datetime
# %n Next line
# %m month -> (e.g 07)
# %I 12Hour (01:)
# %M minutes %H 24Hour (23:) %S Seconds
# %p PM
# %r 01:39:00 PM | %R 13:39 | %X or %T (e.g 13:20:17)
# %a (e.g Mon, Tue) %A (e.g Monday)
# %b or %h (e.g Jan, Jul, Sep) %B (e.g July, March)
# %x (e.g 07/12/25) | %D = (07/12/25)
# %e or %d day -> (e.g 22)
# %C First half digits of the year -> 20
# %g or %y -> Second Half... year (e.g 25) %G or %Y -> Full year
# %F (e.g 2025-07-12)
# %c (e.g Sat Jul 12 13:22:54 2025)

# %u or %w returns 6
# %U or %W returns 27
# %V returns 28

myDate = datetime.now()
seen = 'th'
seeDate = myDate.strftime(f'%B on %d{seen} %a %n%H:%M:%S %p')
# seeDate = myDate.strftime('%B on %d %a')
print(seeDate)








'''
test_Work = [4, 2, 8, 1, 3, 7, 0]
# print(*nums, sep=', ')
# print(*nums[::-1], sep=', ') # Everything reversely 
# [:2:-1] # Before printing reversely, stop after the index 2
# [2::-1] # Print index 2 then print reversely before index 2
# print(test_Work[1:4:2]) # if it's not counting backwards, the middle [:*:] rep. size otherwise the middle rep. index b4 stop!
# test_Work[4:0:-1] # -> 3 1 8 2 Starting point, ending point, and reversed print
# test_Work[1:5][::-1] # Result is same as above
# print(*nums[::-2], sep=', ') # -1 then count 2 backward at each print -> 4, 1, -1, -3, -2
# test_Work[::2] # -> 4, 8, 3, 0 Prints the first then += 2 and so on
# print(*nums[::-3], sep=', ') # -1 then count 3 backward at each print -> 4, 2, -3 
# print(*test_Work[1:-2], sep=', ') # Start from index 1, then remove the last two elements -> 2, 8, 1, 3

digits = [[4, 2, 5], [7, 1, 9], [1, 6, 8], [2, 0, 3]]
# flat = [[y for y in x] for x in digits] # This will print the 2D array in a 2D array technic
flat = [y for x in digits for y in x] # This will print the 2D array in a 1D array technic
flattened = [[y for y in x [::-1]] for x in digits [::-1]] # Full Reverse display
# print(flattened)

# jaize = 'Tosin'
# print(f'jaize:#<10}') # It'll only display if the string n is less than the number given to display xter (-> Tosin#####) 

# checker = "continue"
# print(checker[3::-1]) # Starts from index 3, then count reversely -> tnoc


def setup():
    nick = {
        'key': 'Tosin',
        'age': 12,
        'people': ['Emmanuel', 12, True]
    }
    # for i in nick['people']:
        # print(i)
    return nick['people']

# setup()
# print(' '.join([str(v) for v in setup()]))
print(' '.join(str(v) for v in setup()))


nums = [7, 1, 2, 5, 4, 6]
new = []
while True:
    if len(nums) == 0:
        break
    heapq.heappush(new, nums[0])
    heapq.heappop(nums)


print(end=None) # Equivalent to -> print(end='\n')


def working(st: str) -> bool:
    h = (''.join([x for x in st if x.isalnum()]).lower())
    return h == st[::-1]

# nam = "RADAR"
nam = "radar"
print(working(nam))

# testme = [[4, 5, 6], [1, 2, 3], [7, 8, 95]]
testme = [["Test", "set", "For"], ["All", "Present", "Folks"], ["Check", "Now", "At_once"]]
# testme[2].remove("Now")
# testme[1].pop(-1) # removes testme[1][2] -> 3
# testme[1].remove(3) # removes testme[1][2] -> 3
# testme[0][1] = testme[0][1].title() -> from set to Set
# testme[0][1] = testme[0][1][::-1] -> tes : reversed
# testme[1][1] = int(testme[1][1]) + 4
# testme[1][1] = str(testme[1][1])


# num_String = "4-5-1-2-5-4-1-2-7-5-6-5-8-4-4-5"
name_String = "Johsheph"
print(name_String)

# name_String = name_String.replace('h', '', 2)

# name_String = name_String.replace('h', '', 1) # Point is, incase you're asked to remove middle xter having more than one count
# name_String = name_String.replace('s', 's/', 1)
# filt = name_String.split('/')
# second = filt[1].removeprefix('h')
# filt = filt[0] + second

print(filt)



for i in range(len(testme)):
    print('[', end='')
    for j in range(len(testme[i])):
        print(testme[i][j], end='')
        if j == 0 or j == 1:
            print(end=', ')
    print(']', end=None)


'''


'''
try:
    stuff = int(input('Enter a number: '))
    print(stuff)
except ValueError:
    print('There was a value Error...')
except TypeError:
    print('There was a type Error...')
else: # When it's successful
    print('Exception closing...')
finally: # Regardless of the outcome
    print('Exception finished...')
'''







