
score = 0
for line in open("input.txt", "r"):

    rhs = [*line[slice(0, len(line)//2)]]
    lhs = [*line[slice(len(line)//2, len(line)-1)]]

    for c in rhs:
        if c in lhs:
            score += (ord(c)-38)%58
            break
print(score)
