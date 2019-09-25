from collections import deque

def bfs(start, dst, N):

    Q = deque()
    Q.append(start)
    move = ((-2,1), (-1,2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    while Q:
        v = Q.popleft()
        for k in move:
            wy, wx = v[0] + k[0], v[1] + k[1]
            if 0 <= wy < N and 0 <= wx < N and not D[wy][wx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sta = list(map(int, input().split()))
    dst = list(map(int, input().split()))
    D = [[0 for _ in range(N)] for _ in range(N)]