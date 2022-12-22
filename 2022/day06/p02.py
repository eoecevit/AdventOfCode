file = open("input.txt", "r")

s = []
i = 0

while 1:
    char = file.read(1)
    if not char:
        break
    
    if char in s:
        pos = s.index(char)
        s = s[pos+1:]
    elif len(s) == 14:
        print(i)
        break
    s.append(char)
    i += 1
    


file.close()