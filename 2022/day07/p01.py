
cdir = root = {}
inf = []

for line in open("input.txt", "r"):
    
    command = line.split()
    
    if "$" in line:
        if "cd" == command[1]:
            if "/" == command[2]:
                cdir = root
                inf = []
            elif ".." == command[2]:
                cdir = inf.pop()
            else:
                if command[2] not in cdir:
                    cdir[command[2]] = {}
                inf.append(cdir)
                cdir = cdir[command[2]]
    else:
        info, name = line.split()
        if info == "dir":
            if name not in cdir:
                cdir[name] = {}
        else:
            cdir[name] = int(info)

def calc(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    anz = 0
    for child in dir.values():
        s, a = calc(child)
        size += s
        anz += a
    if size <= 100000:
        anz += size
    return (size, anz)

print(calc()[1])