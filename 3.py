def hamming(p, t):
    if len(p) != len(t):
        return None

    return sum(p[i] != t[i] for i in range(len(p)))


pattern = input()
text = input()
d = int(input())

ans = []

for i in range(len(text) - len(pattern) + 1):
    if hamming(pattern, text[i:i+len(pattern)]) <= d:
        ans.append(i)

for k in ans:
    print(k, end=' ')