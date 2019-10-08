n, k = map(int, input().split())
MIN = 100000
coin = [0] * n
for i in range(n):
    coin[i] = int(input())
    MIN = min(coin[i], MIN)

dp = [0] * ((k // MIN) + 1)

# for i in range(len(dp)):
#     for j in range(len(coin)):
