f = open("day1Text.txt", "r")
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
    
result = map(sum, calorieList)
    
result = list(result)

result.sort()

print("Value of elf with most amount of calories:", result[-1])

topThreeValue = result[-1] + result[-2] + result[-3]
print("Calories carried by the top three elves in total:", topThreeValue)
