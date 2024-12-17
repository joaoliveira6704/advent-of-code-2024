def counter(posY,posX,lines):
    counter = 0
    if posY == 0 and posX == 1:
        for i in range(len(lines)):
            for j in range(len(lines[i])-3):
                check = lines[i][j] + lines [i][j+1] + lines[i][j+2] + lines[i][j+3]
                if check == "XMAS"  or check == "SAMX":
                    print("Found XMAS")
                    counter+=1
    elif posY == -1 and posX == 0:
        for i in range(len(lines)-3):
            for j in range(len(lines[i])):
                check = lines[i][j] + lines [i+1][j] + lines[i+2][j] + lines[i+3][j]
                if check == "XMAS"  or check == "SAMX":
                    print("Found XMAS")
                    counter+=1
    elif posY == -1 and posX == 1:
        for i in range(len(lines)-3):
            for j in range(len(lines[i])-3):
                check = lines[i][j] + lines [i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
                if check == "XMAS"  or check == "SAMX":
                    print("Found XMAS")
                    counter+=1
    return counter
    

with open(".\\day4\\input.txt") as file:
    lines = [list(line.strip()) for line in file]

count1 = 0
count2 = 0
count3 = 0
count4 = 0

count1 = counter(0,1, lines) # Direita
count2 = counter(-1,0, lines) #Baixo
count3 = counter(-1,1, lines) # Diagonal
for row in lines:
    row.reverse()
count4 = counter(-1,1, lines) # Diagonal inversa

total = count1+count2+count3+count4

print(total)