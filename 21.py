money = int(input())
coins = [int(x) for x in input().split(',')]

d = [1e18 for i in range(money + max(coins) + 1)]
d[0] = 0

for i in range(money+1):
    for coin in coins:
        d[i + coin] = min(d[i + coin], d[i] + 1)

print(d[money])