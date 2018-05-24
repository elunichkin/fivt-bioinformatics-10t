n = int(input())

a = [0] * 2 * n
seq = []


def universal(t, p):
    if t > n:
        if n % p == 0:
            for j in range(1, p + 1):
                seq.append(a[j])
    else:
        a[t] = a[t - p]
        universal(t + 1, p)
        for j in range(a[t - p] + 1, 2):
            a[t] = j
            universal(t + 1, t)


universal(1, 1)

f = open('output.txt', 'w')
f.write(''.join(str(d) for d in seq))
f.close()