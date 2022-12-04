


class ProcessIt:
    def __init__(self):
        self.file = open("/mnt/d/c++ advent of code 2022/day 01/data.txt")
        self.sumList = []
        self.templist = []
        #listWhereNewline = []
        total = 0
        for line in self.file.readlines():
            self.templist.append(line)
            #print(self.templist)
            #for i in range(0, len(self.templist)):
            #    if self.templist[i] == "\n":
            #        j = i
            #        for x in range(j, i):
            #            total = total + self.templist[x]
            #
            #        self.sumList.append(total)
                    #total = 0
        for line in self.templist:
            if line == "\n":
                self.sumList.append(total)
                total = 0
                continue
            else:
                total = total + int(line.strip())

        #print(self.sumList)


        


obj1 = ProcessIt()
print("The most calories are:", max(obj1.sumList))
max1 = max(obj1.sumList)
obj1.sumList.remove(max1)
max2 = max(obj1.sumList)
obj1.sumList.remove(max2)
max3 = max(obj1.sumList)

print("The top 3 sum is:", max1+max2+max3)

