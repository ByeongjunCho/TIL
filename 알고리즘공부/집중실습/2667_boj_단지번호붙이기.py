from collections import deque
N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

def BFS(v, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    Q = deque([v])
    visit[v[0]][v[1]] = 1
    while Q:
        v = Q.popleft()
        for i in range(4):
            wy, wx = v[0] + dy[i], v[1] + dx[i]
            if 0 <= wy < N and 0 <= wx < N and not visit[wy][wx] and arr[v[0]][v[1]]:
                visit[wx][wy] = num
                Q.append([wy, wx])

danji = 1
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            BFS([i,j], danji)
            danji += 1

print(danji-1)
S = []
for i in range(1, danji):
    S.append(visit.count(i))
S.sort()
for i in range(len(S)):
    print(S[i])