
cdir = root = {}
stack = []

for line in open("input.txt", "r"):
    if "$" in line:
       if "c" in line:
        adir = line.split()[2]
        if adir == "/":
                cdir = root
                stack = []
        elif adir == "..":
                cdir = stack.pop()
        else:
            if adir not in cdir:
                cdir[adir] = {}
            stack.append(cdir)
            cdir = cdir[adir]
    
    else:
        inf, name = line.split() 
        if inf == "dir":
            if name not in cdir:
                cdir[name] = {}
        else:
            cdir[name] = int(inf)


def solve(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)

print(solve()[1])
        
