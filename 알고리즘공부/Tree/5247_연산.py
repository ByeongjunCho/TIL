T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    used = (1, -1, 2, -10)
    dp = [[1000001 for _ in range(M+1)] for _ in range(5)]