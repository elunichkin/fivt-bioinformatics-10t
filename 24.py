s = input()
t = input()

n, m = len(s), len(t)

c = {}
d = -5

with open('input.txt', 'r') as inf:
    letters = [x for x in inf.readline().split()]
    for i in range(len(letters)):
        cur = [y for y in inf.readline().split()]
        c[cur[0]] = {}
        for j in range(1, len(cur)):
            c[cur[0]][letters[j-1]] = int(cur[j])

F = [[0 for x in range(m+1)] for y in range(n+1)]

print(n, m)

for i in range(1, n+1):
    for j in range(1, m+1):
        if i%10 == 0 and j%100 == 0: print(i, j)
        match = F[i-1][j-1] + c[s[i-1]][t[j-1]]
        delete = max([F[i-k][j] + d * k for k in range(1, i+1)])
        insert = max([F[i][j-l] + d * l for l in range(1, j+1)])
        F[i][j] = max(match, delete, insert, 0)


als, alt, maxi, maxj = "", "", 0, 0

for i in range(n+1):
    for j in range(m+1):
        if F[i][j] > F[maxi][maxj]:
            maxi, maxj = i, j

i, j = maxi, maxj

while i > 0 and j > 0:
    if F[i][j] == 0:
        break
    sc, scd, scu, scl = F[i][j], F[i-1][j-1], F[i][j-1], F[i-1][j]
    if sc == scd + c[s[i-1]][t[j-1]]:
        als, alt, i, j = s[i-1] + als, t[j-1] + alt, i-1, j-1
    elif sc == scl + d:
        als, alt, i = s[i-1] + als, "-" + alt, i-1
    elif sc == scu + d:
        als, alt, j = "-" + als, t[j-1] + alt, j-1

with open('output.txt', 'w') as ouf:
    ouf.write(str(F[maxi][maxj]) + "\n")
    ouf.write(als + "\n")
    ouf.write(alt)