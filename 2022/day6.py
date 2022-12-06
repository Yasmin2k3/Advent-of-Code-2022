def repetition(x):
    for char in x:
        x=x[1:]
        if char in x: 
            return False
    return True

with open('input.txt', "r") as f:
    data = f.read().strip()
    
    for i in range (0, len(data)):
        buffer = data[i:i+4]
        if repetition(buffer):
            print("star 1:", i+4)
            break
    for y in range (0, len(data)):
        messageBuffer = data[y:y+14]
        if repetition(messageBuffer):
            print("star 2:", y + 14)
            break