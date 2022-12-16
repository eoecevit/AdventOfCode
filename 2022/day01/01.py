#/bin/python

file = open("input.txt", "r")
l = file.readlines()

max = 0
curr = 0
for line in l:
    split = line.split('\n')
    if(split[0].isdigit()):
        curr += int(line)
        if(max < curr):
            max = curr
    else:
        curr = 0
        
print(max)