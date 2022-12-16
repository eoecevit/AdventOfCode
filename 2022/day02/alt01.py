
score = 0
for line in open("input.txt", "r"):
    x, y = line.split()
    
    x = ord(x) - ord('A')
    y = ord(y) - ord('X')

    if x == y:
        score += 3
    elif ( y - x )%3 == 1:
        score += 6

    score += y +1

print(score)