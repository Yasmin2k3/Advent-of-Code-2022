f = open("day2Text.txt", "r")
sr = f.read()
f.close()

rawInput = sr.split("\n")
instructions = list(map(lambda x: x.split(" "), rawInput))

def partOne():
    opponentSolutions = ["C", "A", "B"]
    santaSolutions = ["X", "Y", "Z"]

    points = 0

    for a in instructions:
        points += santaSolutions.index(a[1]) + 1
        
        if a[1] == santaSolutions[opponentSolutions.index(a[0])]:
            points += 6
        elif a[1] == santaSolutions[opponentSolutions.index(a[0])-1]:
            points += 3
            
    return points

def partTwo():
    solutions = ["A", "B", "C"]
    points = 0
    
    for a in instructions:
        if a[1] == "X":  
            points += ((solutions.index(a[0])-1) % len(solutions)) + 1
        elif a[1] == "Y":
            points += solutions.index(a[0]) + 4
        elif a[1] == "Z":
            points += ((solutions.index(a[0])+1) % len(solutions)) + 7
        
    return points
        
print("total points:", partOne())

print("new total points:", partTwo())