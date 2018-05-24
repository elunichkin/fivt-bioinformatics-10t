import itertools


def hamming(p, t):
    if len(p) != len(t):
        return None

    return sum(p[i] != t[i] for i in range(len(p)))


def reverse_comp(s):
    t = []
    for i in range(len(s)):
        if s[i] == 'A':
            t.append('T')
        if s[i] == 'T':
            t.append('A')
        if s[i] == 'C':
            t.append('G')
        if s[i] == 'G':
            t.append('C')

    return ''.join(t[::-1])


text = input()
k, d = [int(x) for x in input().split()]

ss = {''.join(x): 0 for x in itertools.product(['A', 'C', 'G', 'T'], repeat=k)}

for i in range(len(text) - k + 1):
    for j in ss.keys():
        if hamming(text[i:i+k], j) <= d:
            ss[j] += 1
        if hamming(text[i:i+k], reverse_comp(j)) <= d:
            ss[j] += 1

ans = (0, [])

for km, c in ss.items():
    if c > ans[0]:
        ans = (c, [km])
    elif c == ans[0]:
        ans[1].append(km)

for km in ans[1]:
    print(km, end=' ')