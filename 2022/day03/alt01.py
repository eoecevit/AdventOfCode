
score = 0
for line in open("input.txt", "r"):
    x = len(line)//2
    rhs = line[:x]
    lhs = line[x:]

    c, = set(rhs) & set(lhs)
    score += (ord(c)-64+26)%58
            
print(score)
