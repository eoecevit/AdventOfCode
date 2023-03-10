cwd = root = {}
stack = []

for line in open("input.txt", "r"):
    if "$" in line:
        command = line.split()
        if command[1] == "cd":
            if command[2] == "/":
                cwd = root
                stack = []
            elif command[2] == "..":
                cwd = stack.pop()
            else:
                if command[2] not in cwd:
                    cwd[command[2]] = {}
                stack.append(cwd)
                cwd = cwd[command[2]]
    else:
        (d, n) = line.split()
        if d == "dir":
            if n not in cwd:
                cwd[n] = {}
        else:
            cwd[n] = int(d)

def calc(dir = root):
    if type(dir) is int:
        return (dir, 1)
    size = 0
    anz = 0
    for sub in dir.values():
        (s, a) = calc(sub)
        if()
        size += s
        anz += a
    if size <= 8381165:
        anz += size
    return(size, anz)

print(calc()[1])