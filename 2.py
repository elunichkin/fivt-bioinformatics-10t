genome = input()

skew = 0
ans = (0, [0])

for i in range(len(genome)):
    if genome[i] == 'C':
        skew -= 1
    elif genome[i] == 'G':
        skew += 1

    if skew < ans[0]:
        ans = (skew, [i+1])
    elif skew == ans[0]:
        ans[1].append(i+1)

for k in ans[1]:
    print(k, end=' ')