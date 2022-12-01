f = open("day1Text.txt", "r")
sr = f.read()
f.close()

rawStrings = sr.split("\n")

#part 1:
calorieList = []
calorieElf = []

for a in rawStrings:
    if a == '':
        calorieList.append(calorieElf)
        calorieElf = []
    else:
        calorieElf.append(int(a))

for x in range (len(calorieList)):
    calorieList[x] = sum(calorieList[x])
    
calorieList.sort()
print("Value of elf with most amount of calories:", calorieList[-1])

#part 2:
topThreeValue = calorieList[-1] + calorieList[-2] + calorieList[-3]
print("Calories carried by the top three elves in total:", topThreeValue)
