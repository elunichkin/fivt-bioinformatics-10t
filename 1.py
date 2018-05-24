genome = input()
k, l, t = [int(x) for x in input().split()]

cnt = {genome[i:i+k]: [] for i in range(len(genome) - k + 1)}

for i in range(len(genome) - k + 1):
    cnt[genome[i:i+k]].append(i)

ans = []

for g, v in cnt.items():
    if len(v) < t:
        continue

    for i in range(len(v) - t + 1):
        if v[i+t-1]+k - v[i] <= l:
            ans.append(g)
            break

for k in ans:
    print(k, end=' ')