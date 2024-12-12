list1 = []

f = open(".\\testers\\data.csv", "r")

lines = f.readlines()
i=0
for line in lines:
    fields = line.split(";")
    print(fields)
    list1.append([])
    for field in fields:
        try:
            list1[i].append(int(field))
        except ValueError:
            list1[i].append(int(field.strip("\n")))
    i+=1

#f.close()
print(list1)
unsafe = 0
safe = 0
safeTotal = 0
unsafeTotal = 0
compare = 0
for i in range(len(list1)):
    soma = 0
    unsafe = 0
    safe = 0
    for j in range(len(list1[i])):
        list1[i].sort()
        if j<len(list1[i])-1:
            if list1[i][j] - list1[i][j+1] < 1 or list1[i][j] - list1[i][j+1] > 2:
                unsafe += 1
            elif list1[i][j+1] - list1[i][j] < 1 or list1[i][j+1] - list1[i][j] > 3:
                unsafe += 1
            else:
                safe += 1
        else:
            compare = list1[i][j-1]
            if compare - list1[i][j] < 1 or compare - list1[i][j] > 2:
                unsafe += 1
            elif list1[i][j] - compare < 1 or list1[i][j] - compare > 3:
                unsafe += 1
            else:
                safe += 1
                
    if unsafe >= 1:
        unsafeTotal += 1
        print(f"line {i+1} unsafe")
    else:
        safeTotal += 1
        print(f"line {i+1} safe")

print(f"Safe: {safeTotal}\nUnsafe: {unsafeTotal}")