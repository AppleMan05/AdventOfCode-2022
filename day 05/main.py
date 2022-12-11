stack1 = ["D","Z","T","H"]
stack2 = ["S","C", "G","T", "W", "R", "Q"]
stack3 = ["H", "C", "R", "N", "Q", "F", "B", "P"]
stack4 = ["Z", "H", "F", "N", "C", "L"]
stack5 = ["S", "Q", "F", "L", "G"]
stack6 = ["S", "C", "R", "B", "Z", "W", "P", "V"]
stack7 = ["J", "F", "Z"]
stack8 = ["Q", "H", "R", "Z", "V", "L", "D"]
stack9 = ["D", "L", "Z", "F", "N", "G", "H", "B"]

"""  
        [H]         [S]         [D]
    [S] [C]         [C]     [Q] [L]
    [C] [R] [Z]     [R]     [H] [Z]
    [G] [N] [H] [S] [B]     [R] [F]
[D] [T] [Q] [F] [Q] [Z]     [Z] [N]
[Z] [W] [F] [N] [F] [W] [J] [V] [G]
[T] [R] [B] [C] [L] [P] [F] [L] [H]
[H] [Q] [P] [L] [G] [V] [Z] [D] [B]
 1   2   3   4   5   6   7   8   9 
 """

def moveFunction(numberToMove, StackFromWhereToMove, DestinationStack):
    for i in range(1, numberToMove+1):
        #these elements are picked up
        DestinationStack.insert(0, StackFromWhereToMove[0])
        #print(i, sourceStack, destinationStack)
        del StackFromWhereToMove[0]
    #del StackFromWhereToMove[0:numberToMove]

def determineStack(input):
    global stack1
    global stack2
    global stack3
    global stack4
    global stack5
    global stack6
    global stack7
    global stack8
    global stack9
    if input == 1:
        return stack1
    elif input == 2:
        return stack2
    elif input == 3:
        return stack3
    elif input == 4:
        return stack4
    elif input == 5:
        return stack5
    elif input == 6:
        return stack6
    elif input == 7:
        return stack7
    elif input == 8:
        return stack8
    elif input == 9:
        return stack9

file = open("day 05/data.txt")
functionList = []
for line in file.readlines():
    x = line.split()
    #print(x)
    number = x[1]
    sourceStack = determineStack(int(x[3]))
    destinationStack = determineStack(int(x[5].strip()))
    moveFunction(int(number), sourceStack, destinationStack)
#print(range(1,1))
print(stack1[0], stack2[0], stack3[0], stack4[0], stack5[0], stack6[0], stack7[0], stack8[0], stack9[0])

#Part 1 done
stack1 = ["D","Z","T","H"]
stack2 = ["S","C", "G","T", "W", "R", "Q"]
stack3 = ["H", "C", "R", "N", "Q", "F", "B", "P"]
stack4 = ["Z", "H", "F", "N", "C", "L"]
stack5 = ["S", "Q", "F", "L", "G"]
stack6 = ["S", "C", "R", "B", "Z", "W", "P", "V"]
stack7 = ["J", "F", "Z"]
stack8 = ["Q", "H", "R", "Z", "V", "L", "D"]
stack9 = ["D", "L", "Z", "F", "N", "G", "H", "B"]

def moveFunction2(number, source, destination):
    temp = source[0:number]
    temp.reverse()
    del source[0:number]
    #the list has been sliced
    for i in temp:
        destination.insert(0, i)
file = open("day 05/data.txt")
for line in file.readlines():
    x = line.split()
    #print(x)
    number = x[1]
    sourceStack = determineStack(int(x[3]))
    destinationStack = determineStack(int(x[5].strip()))
    moveFunction2(int(number), sourceStack, destinationStack)
#print(range(1,1))
print(stack1[0], stack2[0], stack3[0], stack4[0], stack5[0], stack6[0], stack7[0], stack8[0], stack9[0])

#answer = CQQBBJFCS