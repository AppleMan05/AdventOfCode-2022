def getPriority(input):
    priorityList = [{"a"},{"b"},{'c'},{'d'},{'e'},{'f'},{'g'},{'h'},{'i'},{'j'},{'k'},{'l'},{'m'},{'n'},{'o'},{'p'},{'q'},{'r'},{'s'},{'t'},{'u'},{'v'},{'w'},{'x'},{'y'},{'z'},{'A'},{'B'},{'C'},{'D'},{'E'},{'F'},{'G'},{'H'},{'I'},{'J'},{'K'},{'L'},{'M'},{'N'},{'O'},{'P'},{'Q'},{'R'},{'S'},{'T'},{'U'},{'V'},{'W'},{'X'},{'Y'},{'Z'}]
    priority = priorityList.index(input) + 1
    return priority

compartment1 = []
compartment2 = []

file = open("/mnt/d/c++ advent of code 2022/day 03/data.txt")
for line in file.readlines():
    x = len(line)
    string1 = slice(0, len(line)//2)
    string2 = slice(len(line)//2, len(line))
    compartment1.append(line[string1])
    compartment2.append(line[string2])

commonThings = []

def getCommon(input1, input2):
    set1 = set()
    set2 = set()
    for character in input1:
        set1.add(character)
    for character in input2:
        set2.add(character)
    commonThings.append(set.intersection(set1, set2))

for i in range(0, len(compartment1)):
    getCommon(compartment1[i], compartment2[i])

#print(commonThings)
total = 0
for i in commonThings:

    total = total + getPriority(i)

print(total)

#Part 1 is done
tmp = []
x = 0
def getChunk(list):
    global x
    #print(len(list))
    while x+3 <= len(list):
        #tmp.append(list[x])
        #tmp.append(list[x+1])
        #tmp.append(list[x+2])
        tmp.append([list[x], list[x+1], list[x+2]])
        #print(x)
        x = x + 3
        if x >= len(list):
            break
tmp2 = []
file = open("/mnt/d/c++ advent of code 2022/day 03/data.txt")
for line in file.readlines():
    tmp2.append(line.strip())

getChunk(tmp2)
#print(tmp2)
#print(tmp)
#ok so ive managed to sort the list according to the problem
commonThings2 = []
def getCommon2(i1, i2, i3):
    set1 = set()
    set2 = set()
    set3 = set()
    for character in i1:
        set1.add(character)
    for character in i2:
        set2.add(character)
    for character in i3:
        set3.add(character)
    commonThings2.append(set.intersection(set1, set2, set3))

for i in range(0, len(tmp)):
    getCommon2(tmp[i][0], tmp[i][1], tmp[i][2])

#print(commonThings2)
    
total = 0
for i in commonThings2:

    total = total + getPriority(i)

print(total)