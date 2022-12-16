
file = open("input.txt", "r")


A = 1
B = 2
C = 3

WIN = 6
DRAW = 3
LOSS = 0

score = 0
for line in file:
    
    if(line[0] == 'A'):
        if(line[2] == 'Y'):
            score += (A + DRAW)
        elif(line[2] == 'Z'):
            score += (B + WIN)
        elif(line[2] == 'X'):
            score += (C + LOSS)

    elif(line[0] == 'B'):
        if(line[2] == 'X'):
            score += (A + LOSS)
        elif(line[2] == 'Y'):
            score += (B + DRAW)
        elif(line[2] == 'Z'):
            score += (C + WIN)

    elif(line[0] == 'C'):
        if(line[2] == 'Z'):
            score += (A + WIN)
        elif(line[2] == 'X'):
            score += (B + LOSS)
        elif(line[2] == 'Y'):
            score += (C + DRAW)
        

print(score)
