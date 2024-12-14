import re

with open(".\\day3\\data.txt") as file:
    lines = file.read()
    strfind = ""
    for line in lines:
        strfind += line

findlastDo = strfind.rfind("do()")
newText = strfind[findlastDo:]
lastDont = newText.find("don't()")

if lastDont == -1:
    newText = strfind
else:
    lastPos = findlastDo+lastDont
    newText = strfind[:lastPos]

mulList = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", newText)
content = re.findall(r"(?<=don't\(\))(.*?)(?=do\(\))", newText, re.DOTALL)

dont = []
for section in content:
    dont += re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", section)

dont = [(int(x), int(y)) for x,y in dont]
mulList = [(int(x), int(y)) for x,y in mulList]


for duplicate in mulList[:]:
    if duplicate in dont:
        mulList.remove(duplicate)
        dont.remove(duplicate)

total_sum = 0
for position in mulList:
    total_sum += int(position[0]) * int(position[1])

print(total_sum)