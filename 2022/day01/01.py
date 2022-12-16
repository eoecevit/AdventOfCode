#/bin/python

file = open("input.txt", "r")

cal = [0]
for line in file:
    split = line.split('\n')
    
    if(split[0].isdigit()):
        cal[-1] += int(line)

    else:
        cal.append(0)
  
print(max(cal))