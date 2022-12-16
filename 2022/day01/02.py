#/bin/python

file = open("input.txt", "r")
l = file.readlines()

cal = [0]
for line in l:
    split = line.split('\n')
    
    if(split[0].isdigit()):
        cal[-1] += int(line)

    else:
        cal.append(0)

cal.sort()
print(sum(cal[-3:]))