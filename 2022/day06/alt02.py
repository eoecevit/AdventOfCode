line = open("input.txt", "r")
line = line.readline()

for x in range(14, len(line)):
    if len(set(line[x - 14:x])) == 14:
        print(x)
        exit(0)