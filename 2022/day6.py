def repetition(x):
    for char in x:
        x=x[1:]
        if char in x: 
            return False
    return True

def bufferCheck(l, n):
    for i in range (0, len(l)):
        buffer = l[i:i+n]
        if repetition(buffer):
            return i+n


with open('input.txt', "r") as f:
    data = f.read().strip()
    
    print("star 1:", bufferCheck(data, 4))
    print("star 2:", bufferCheck(data, 14))
