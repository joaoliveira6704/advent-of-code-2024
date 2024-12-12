n = 50

for i in range(n+1):
    print(" " * (n - i) + "*" * (i +1)+ "*" * (i))

for i in range(n-1,-1,-1):
    print(" " * (n - i) + "*" * (i +1)+ "*" * (i))



    for i in range(len(fields)):
        list1.append([])
        for j in range(len(fields)):
            list1[i].append(int(fields[j]))
            if j == 4:
                list1[i].append(int(fields[j].strip("\n")))