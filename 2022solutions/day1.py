f = open("C:\\Users\\yasmi\\Documents\\Python\\AdventofCode\\AdventofCodeText\\2022\day1.txt", "r")
sr = f.read()
f.close()

rawStrings = sr.split("\n")

calorieList = []
calorieElf = []

for a in rawStrings:
    if a == '':
        calorieList.append(calorieElf)
        calorieElf = []
    else:
        calorieElf.append(int(a))

for x in range (len(calorieList)):
    totalCalorie = 0
    for y in calorieList[x]:
        totalCalorie += y
    calorieList[x] = totalCalorie
    
calorieList.sort()
print("Value of elf with most amount of calories:", calorieList[-1])

topThreeValue = calorieList[-1] + calorieList[-2] + calorieList[-3]
print("Calories carried by the top three elves in total:", topThreeValue)