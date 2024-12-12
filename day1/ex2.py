list1 = []
list2 = []

f = open(".\\day1\\data.csv", "r")

lines = f.readlines()

for line in lines:
    fields = line.split(";")
    list1.append(int(fields[0]))
    list2.append(int(fields[1].strip("\n")))

f.close()

list1.sort()
list2.sort()

numSum = 0
for i in range(len(list1)):
    numCount = list1[i]
    numSum += (list2.count(numCount) * numCount)

print(f"\n\nFinal distance = {numSum}")

