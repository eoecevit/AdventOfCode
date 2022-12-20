

badges = []
shortest = ""
score = 0
for line in open("input.txt", "r"):
    badges.append(line.split("\n")[0])
    if (len(badges) == 3):
        c, = set(badges[0]) & set(badges[1]) & set(badges[2])
        score += (ord(c)-64+26)%58
        badges = []
print(score)
