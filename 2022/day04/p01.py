

c = 0
for pairs in open("input.txt", "r"):
    one, two, three, four = map(int, pairs.replace("-", ",").split(","))
    if one <= three and two >= four or three <= one and four >= two:
        c +=1

print(c)