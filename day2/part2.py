counter = 0 

def is_increasing(list1):
    for i in range(len(list1)-1):
        diff = list1[i+1]-list1[i]
        if diff not in [1, 2, 3]: 
            return False
    return True  

def is_decreasing(list1):
    for i in range(len(list1)-1):
        diff = list1[i]-list1[i+1]
        if diff not in [1, 2, 3]: 
            return False
    return True  

def can_be_safe_with_dampener(list1):
    for i in range(len(list1)):
        modified_list = list1[:i]+list1[i+1:]
        if is_increasing(modified_list) or is_decreasing(modified_list):
            return True
    return False


def check_line(line):
    list1 = line.split(" ")
    for  i in range(len(list1)):
        list1[i] = int(list1[i].strip())

    if is_increasing(list1) or is_decreasing(list1):
        return True
    elif can_be_safe_with_dampener(list1):
        return True
    return False 

with open(".\\day2\\input.txt") as file:
    lines = file.readlines()
    for line in lines:
        if check_line(line):  
            print(line.strip(), "line safe")
            counter += 1 
        else:
            print(line.strip(), "line unsafe")

print(f"Total safe reports: {counter}")