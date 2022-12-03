def splitString(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

def priority(char):
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    itemValue = []
    
    if char.isupper():
        itemValue.append(UPPERCASE.index(char) + 27)
    else:
        itemValue.append(LOWERCASE.index(char) + 1)
    
    return sum(itemValue)

f = open('day3.txt', "r")
sr = f.read()
f.close()
sr = sr.split("\n")

items = list(map(splitString, sr))

priorityItems = []

for i in items:
    for x in i[0]:
        if i[1].__contains__(x):
            priorityItems.append(x)
            break

print("star 1:", sum(list(map(priority, priorityItems))))

#part 2
group = 1
badges = []
for x in range (0, len(sr), 3):    
    for y in sr[x]:
        if sr[x+1].__contains__(y) and sr[x+2].__contains__(y):
            badges.append(y)
            break
        
print("star 2:", sum(list(map(priority, badges))))