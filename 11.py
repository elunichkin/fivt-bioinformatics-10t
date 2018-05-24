s = []

with open('input.txt', 'r') as inf:
    k = int(inf.readline())

    for line in inf:
        s.append(line)

for i in range(len(s) - 1):
    s[i] = s[i][:-1]

g = [[] for x in range(len(s))]
deg = [0 for x in range(len(s))]

for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            continue
        if s[i][1:] == s[j][:-1]:
            g[i].append(j)
            deg[i] += 1
            deg[j] += 1

ans = []

v = 0
for u in range(len(s)):
    if deg[u] % 2 == 1 and len(g[u]) > 0:
        v = u
        break

st = [v]
while len(st) > 0:
    w = st[-1]
    for u in range(len(s)):
        if u in g[w]:
            st.append(u)
            g[w].remove(u)
            break
    if w == st[-1]:
        st.pop()
        ans.append(w)

with open('output.txt', 'w') as ouf:
    ouf.write(s[ans[-1]])
    for a in reversed(ans[:-1]):
        ouf.write(s[a][-1])