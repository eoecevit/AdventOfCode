
stack = [[],[],[],[],[],[],[],[],[]]
x = 0
chunks = ""
for line in open("input.txt", "r"):
    line = line.split("\n")[0]
    index = 0
    if len(line) == 0:
        x = 1
        continue
    if x == 0:
        l = int((len(line)-8)/3)
        for n in range(0, l):
            if line[index:index+3] != '   ' and ord(line[index+1:index+2]) >= 65:
                stack[n].append(line[index:index+3])
            index += 4
    else:
        words = line.split(" ")
        t = int(words[1]) #how often(times)
        f = int(words[3])-1 #from
        w = int(words[5])-1 #where
        
        for n in range(t):
            crate = stack[f][t-1-n]
            stack[f].pop(t-1-n)
            stack[w].insert(0, crate)
    

mesg = ""
for n in range(0, 9):
    mesg += stack[n][0][1]
print(mesg)