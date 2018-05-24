perm = [int(x) for x in input()[1:-1].split()]

perm = [0] + perm + [len(perm) + 1]

brkpts = 0

for i in range(len(perm) - 1):
    if perm[i+1] - perm[i] != 1:
        brkpts = brkpts + 1

print(brkpts)