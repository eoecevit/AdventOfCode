
score = 0
for line in open("input.txt", "r"):
    x, y = line.split()
    
    x = ord(x) - ord('A')
    y = ord(y) - ord('X')

    if y == 1:
        score += (3 + x) + 1
    elif y == 2:
        score += ( 6 + ( x + 1 ) % 3) + 1
    else:
        score += (x-1) % 3 + 1

print(score)