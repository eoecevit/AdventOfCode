
file = open("input.txt", "r")

me = dict({'X': 'A', 'Y':'B', 'Z':'C'})

A = 1
B = 2
C = 3

WIN = 6
DRAW = 3
LOSS = 0

score = 0
for line in file:
    
    if(line[0] == 'A'):
        if(me[line[2]] == 'A'):
            score += (A + DRAW)
        elif(me[line[2]] == 'B'):
            score += (B + WIN)
        elif(me[line[2]] == 'C'):
            score += (C + LOSS)

    elif(line[0] == 'B'):
        if(me[line[2]] == 'A'):
            score += (A + LOSS)
        elif(me[line[2]] == 'B'):
            score += (B + DRAW)
        elif(me[line[2]] == 'C'):
            score += (C + WIN)

    elif(line[0] == 'C'):
        if(me[line[2]] == 'A'):
            score += (A + WIN)
        elif(me[line[2]] == 'B'):
            score += (B + LOSS)
        elif(me[line[2]] == 'C'):
            score += (C + DRAW)
        

print(score)
