def rvsd(p):
    return [-x for x in reversed(p)]


ouf = open('output.txt', 'w')


def prnt(p):
    ouf.write('(')
    for i in range(len(p) - 1):
        ouf.write(str(format(p[i], '+')) + ' ')
    ouf.write(str(format(p[-1], '+')))
    ouf.write(')\n')


perm = [int(x) for x in input()[1:-1].split()]

for i in range(len(perm)):
    if perm[i] != i+1:
        if i+1 in perm:
            l = perm.index(i+1)
        else:
            l = perm.index(-i-1)
        perm[i:l+1] = rvsd(perm[i:l+1])
        prnt(perm)
    if perm[i] == -i-1:
        perm[i] = i+1
        prnt(perm)

ouf.close()