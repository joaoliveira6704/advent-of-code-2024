def counter(lines):
    counter = 0
    for i in range(len(lines)-2):
        for j in range(len(lines)-2):
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] == "MAS" and lines[i+2][j] + lines[i+1][j+1] + lines[i][j+2] == "SAM":
                counter+=1
            elif lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] == "SAM" and lines[i+2][j] + lines[i+1][j+1] + lines[i][j+2] == "SAM":
                counter+=1
            elif lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] == "MAS" and lines[i+2][j] + lines[i+1][j+1] + lines[i][j+2] == "MAS":
                counter+=1
            elif lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] == "SAM" and lines[i+2][j] + lines[i+1][j+1] + lines[i][j+2] == "MAS":
                counter+=1
    return counter
    

with open(".\\day4\\input.txt") as file:
    lines = [list(line.strip()) for line in file]

total = counter(lines)

print(total)