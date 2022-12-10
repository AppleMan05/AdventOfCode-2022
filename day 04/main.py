file = open("day 04/data.txt")
group1 = []
group2 = []
for line in file.readlines():
    x = line.split(",")
    #print(x)
    group1.append(x[0])
    group2.append(x[1].strip())

group1set = []
group2set = []
def convertFunction(input1):
    global set1
    i1 =input1.split("-")
    set1 = set()
    for i in range(int(i1[0]), int(i1[1])+1):
        set1.add(i)

for i in group1:
    convertFunction(i)
    group1set.append(set1)

for i in group2:
    convertFunction(i)
    group2set.append(set1)

#print(group1set)
#length of group1 and group2 must be the same
total = 0
for i in range(0, len(group1set)):
    x = set.intersection(group1set[i], group2set[i])
    """ if len(x) == len(group1set[i]):
        print("aha!", i)
    elif len(x) == len(group2set[i]):
        print("hmm", i) """
    """ if len(x) != 0:
        print(x) """
    if x == group2set[i]:
        #print("bam", i+1, x)
        total += 1
    elif x == group1set[i]:
        total +=1

print(total)

#part 1 done
total2=0
for i in range(0, len(group1set)):
    x = set.intersection(group1set[i], group2set[i])
    if len(x) != 0: 
        total2 += 1

print(total2)