

c = 0
for pairs in open("input.txt", "r"):
    one, two, three, four = map(int, pairs.replace("-", ",").split(","))
    
    a = set(range(one, two + 1))
    b = set(range(three, four + 1))
    if a & b:
        c += 1
    

print(c)

