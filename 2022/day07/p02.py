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

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

t = size() - 40_000_000

def solve(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans

print(solve())