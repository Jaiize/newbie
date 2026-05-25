import re as rex
import heapq
from collections import deque, Counter
from itertools import permutations, zip_longest
from datetime import datetime

#py -3 -m venv <name> for environment creation
# python -u "C:\Users\JosephET\Documents\VS Code\Workspace\Testwork\pyme.py"
# & C:/Users/JosephET/Envs/MyVirEnv/Scripts/Activate.ps1



# controller = rex.compile(r"([a-z])\1")
# controller = rex.compile(r"(\d)\1")
# controller = rex.compile(r"(\d)\1\1")

# prior index are accted for (except the xter in-between) but idx of the last two digits is only provided (e.g "Passw652rd "gives indexes of ss + 52)
# controller = rex.compile(r"([a-z])\1.*(.)\d")  # first identical xter + any xter + first identical digit / xter 


# controller = rex.compile(r"([a-z])\1+([a-z])+(\d)") # first identical xter + any xter + first one digit 
controller = rex.compile(r"(\d){3}")

# testStr = "Passw94rd"
# testStr = "Passqzsxoh77rd"
# testStr = "Passohkkrd"
# testStr = "Passw6665rd"
testStr = "Passw652rd"




if controller.search(testStr):
    regs = controller.search(testStr).regs
    grp = controller.search(testStr).group()
    print(f"Yes | {grp} | {regs}")
else:
    print("No", controller.search(testStr))






words = ["acca", "bbbb", "caca"]
# words = ["acca", "b", "caca"] # infinit loop
target = "aba"

def formTarget(wor: list[str], tar: str) -> int:
    step = 0
    counter = 0
    j = 0
    res = []
    while True:
        if wor[j].find(tar[step]) != -1:
            counter += 1
            idx = wor[j].find(tar[step])
            wor[j] = wor[j].replace(wor[j][idx], '', 1)
        j = (j + 1) % len(wor)
        if counter == 0:
            break
        elif counter == len(tar):
            res.append(counter)
            counter = 0
        step = (step + 1) % len(tar)
    return sum(res)
targ = formTarget(words, target)
# print(targ)

ss = {
    'name': 'Tosin',
    'age': 10,
    'kin': ['Gemini', 'Princess-like']
}
print(ss["kin"])
































































                    




















       



    

   





























































print(end=None)
for_date = datetime.now()
# print(for_date.strftime("| %H:%M %b %m %a %d |"))
print(for_date.strftime("| %c |"))

# for_map = map(lambda x, y: x * y, [1, 2, 7, 5], [0, 2, 2, 5])
# print(set(for_map)) # Heap-like storage
# print(list(for_map))



'''
n = [7, 2, 8, 1, 9, 0, 5]
# Both in ascending order

temp: int
jay: int
for i in range(1, len(n)):
    temp = n[i]
    jay = i - 1
    while temp < n[jay] and (jay >= 0):
        n[jay + 1] = n[jay]
        jay = jay - 1
    n[jay + 1] = temp

print(n)
'''

'''
n = [7, 2, 8, 1, 9, 0, 5]
tempo: int
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] > n[j]:
            tempo = n[i]
            n[i] = n[j]
            n[j] = tempo

print(n)
'''
    
