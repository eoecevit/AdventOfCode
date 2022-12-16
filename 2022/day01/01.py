#/bin/python

file = open("input.txt", "r")
l = file.readlines()

cal = [0]
curr = 0
for line in l:
    split = line.split('\n')
    if(split[0].isdigit()):
        curr += int(line)

    else:
        cal[-1] = curr
        cal.append(0)
        curr = 0
        
print(max(cal))