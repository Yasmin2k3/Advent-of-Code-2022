#very tired so this might be the messiest thing I have done so far
with open('input.txt', "r") as f:
    data = f.read().split("\n")
    
    #cleaning input
    data = list(map(lambda x: x.translate(str.maketrans('', '', 'fromtve')), data))
    data = list(map(lambda x: x.split(), data))
    
    for i in data:
        i[0] = int(i[0])
        i[1] = int(i[1])
        i[2] = int(i[2])
          
#I'll change this later when I look up how to do it better
stackList = {
    1: ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
    2: ['N', 'B', 'L'],
    3: ['J', 'C', 'H', 'T', 'L', 'V'],
    4: ['S', 'P', 'J', 'W'],
    5: ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
    6: ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
    7: ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
    8: ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
    9: ['R', 'P', 'M', 'L', 'H']
    }

for y in data:
    #x is amount to move, n is starting stack, m is end stack
    x = y[0]
    n = y[1]
    m = y[2]
    
    stackList[m].extend(stackList[n][-x:])
        
    #why does this not work!?!??!
    #stackList[n] = stackList[n][: len(stackList[n]) - x]
        
    for a in range (0, x):
        stackList[n].pop()
    
print(stackList[1][-1] + stackList[2][-1] + stackList[3][-1] + stackList[4][-1] + stackList[5][-1] + stackList[6][-1] + stackList[7][-1] + stackList[8][-1] + stackList[9][-1])
    
    
        
    