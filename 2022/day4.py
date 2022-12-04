#In how many assignment pairs does one range fully contain the other?
def assignmentOverlap(x):
    if ((x[0][0] <= x[1][0]) and (x[0][1]) >= (x[1][1])) or ((x[1][0] <= x[0][0]) and (x[1][1] >= x[0][1])):
        return True
    else:
        return False
    
def assignmentOverlap2(i):
    if ((i[0][0] >= i[1][0]) and (i[0][0] <= i[1][1])) or ((i[0][1] >= i[1][0]) and (i[0][0] <= i[1][1])):
        return True
    else:
        return False

with open('input.txt', "r") as f:
    sr = f.read().split("\n")
    
    #formatting
    sr = list(map(lambda x: x.split(","), sr))
    sr = [list(map(lambda x: x.split('-'), x)) for x in sr]
    for a in sr:
        for b in a:
            b[0] = int(b[0])
            b[1] = int(b[1])
            
part1 = list(filter(assignmentOverlap, sr))
part2 = list(filter(assignmentOverlap2, sr))
            
print("part 1:", len(part1))
print("part 2:", len(part2))