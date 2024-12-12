list1 = []
counter =0
def is_increasing(list1):
    print(list1)
    safe = 0
    unsafe = 0
    for i in range(len(list1)):
        if i == len(list1)-1:
            a=list1[i]
            b=list1[i-1]
            c=abs(a-b)
            if c == 1 or c==2 or c==3:
                safe+=1
        else:
            a = list1[i]
            b = list1[i+1]
            print(a,b," Increasing")
            c = b-a
            if c == 1 or c==2 or c==3:
                print(abs(a-b), "safe")
                safe += 1
            elif c == 0:
                print(abs(a-b), "unsafe")
                unsafe +=1
            else:
                unsafe+=1
    
    if unsafe > 0:
        safe = False
    else:
        safe = True

    return safe

def is_decreasing(list1):
    print(list1)
    safe=0
    unsafe=0
    for i in range(len(list1)):
        if i == len(list1)-1:
            a=list1[i]
            b=list1[i-1]
            c=abs(a-b)
            if c == 1 or c==2:
                safe+=1
        else:
            a = list1[i]
            b = list1[i+1]
            print(a,b," Decreasing")
            c = a-b
            if c == 1 or c==2:
                print(abs(a-b), "safe")
                safe +=1
            elif c == 0:
                print(abs(a-b), "unsafe")
                unsafe +=1
            else:
                unsafe+=1
    if unsafe > 0:
        safe = False
    else:
        safe = True
    return safe

def check_line(line):
    list1 = line.split(";")
    for  i in range(len(list1)):
        if i == (len(list1) - 1):
            list1[i] = int(list1[i].strip("\n"))
        else:
            list1[i] = int(list1[i])

    for i in range(2):

            a = list1[i]
            b = list1[i+1]

            if a > b:
                valid = is_decreasing(list1)
                print(valid)
                if valid == False:
                    return False
                else:
                    return True
            elif a < b:
                valid = is_increasing(list1)
                if valid == False:
                    return False
                else:
                    return True
            else:
                return False

    list1=[]

with open("testers/data2.csv") as file:
    lines = file.readlines()
    for line in lines:
        isSafe = check_line(line)
        if isSafe == True:
            print(line, "line safe")
            counter+=1
        else:
            print(line, "line unsafe")

print(counter)