

def calculate(line):
    global myScore, opponentScore
    myDict = {
        "A X" : (3 + 1), 
        "A Y" : (6 + 2), 
        "A Z" : (0 + 3), 
        "B X" : (0 + 1), 
        "B Y" : (3 + 2),
        "B Z" : (6 + 3), 
        "C X" : (6 + 1), 
        "C Y" : (0 + 2),
        "C Z" : (3 + 3)
    }
    opponentDict = {
        "A X" : (0 + 3),
        "A Y" : (3 + 1),
        "A Z" : (6 + 2),
        "B X" : (0 + 1),
        "B Y" : (3 + 2),
        "B Z" : (6 + 3),
        "C X" : (0 + 2),
        "C Y" : (3 + 3),
        "C Z" : (6 + 1)
    }
    myScore = myScore + myDict[line]
    opponentScore = opponentScore + opponentDict[line]

myScore = 0
opponentScore = 0

file = open("data.txt")
#for line in file.readlines():
    #print(line.strip())
#    calculate(line.strip())

#print(myScore)
#print(opponentScore)
#rock(A,X) beats scissor
#paper(B,Y) beats rock
#scissor(C,Z) beats paper

def round2Calculate(a,b):
    if b == "X":
        #we need to lose
        if a == "A": #rock
            myChoice = "Z"
            
        elif a == "B": #paper
            myChoice = "X"
            
        elif a == "C": #scissor
            myChoice = "Y"
            
    elif b == "Y": #draw
        if a == "A":
            myChoice = "X"
        elif a == "B":
            myChoice = "Y"
        elif a == "C":
            myChoice = "Z"

    elif b == "Z": #we win
        if a == "A":
            myChoice = "Y"
        elif a == "B":
            myChoice = "Z"
        elif a == "C":
            myChoice = "X"

    calculate(f'{a} {myChoice}')

for line in file.readlines():
    x = line.split()
    #print(x)
    round2Calculate(x[0], x[1])

print(myScore)
