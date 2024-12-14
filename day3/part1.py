import re

with open(".\\day3\\data.txt") as file:
    lines = file.readlines()
    strfind = ""
    for line in lines:
        strfind += line
    
    mulList = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", strfind)
    print(mulList)

    sum = 0
    mult = 0
    for position in mulList:
        mult = int(position[0]) * int(position[1])
        print(mult)
        sum += mult
print(sum)