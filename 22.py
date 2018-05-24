n, m = [int(x) for x in input().split()]

down = [[int(x) for x in input().split()] for y in range(n)]
input()
right = [[int(x) for x in input().split()] for y in range(n+1)]

d = [[0 for x in range(m+1)] for y in range(n+1)]

for i in range(1, n+1):
    d[i][0] = d[i-1][0] + down[i-1][0]

for j in range(1, m+1):
    d[0][j] = d[0][j-1] + right[0][j-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i-1][j] + down[i-1][j], d[i][j-1] + right[i][j-1])

print(d[n][m])