s = []

with open('input.txt', 'r') as inf:
    k, d = [int(x) for x in inf.readline().split()]

    for line in inf:
        s.append(line.split('|'))

for i in range(len(s) - 1):
    s[i][1] = s[i][1][:-1]

sans = ['', '']

sans[0] += s[0][0]
sans[1] += s[0][1]
for a in range(1, len(s)):
    sans[0] += s[a][0][-1]
    sans[1] += s[a][1][-1]

with open('output.txt', 'w') as ouf:
    ouf.write(sans[0] + sans[1][(len(sans[0])-k-d):])

#