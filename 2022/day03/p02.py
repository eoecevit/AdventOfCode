

badges = []
shortest = ""
score = 0
for line in open("input.txt", "r"):
    badges.append(line.split("\n")[0])
    if (len(badges) == 3):
        for c in badges[0]:
            if c in badges[1] and c in badges[2]:
                print(c)
                print()
                score += (ord(c)-64+26)%58
                break
        badges = []
print(score)
