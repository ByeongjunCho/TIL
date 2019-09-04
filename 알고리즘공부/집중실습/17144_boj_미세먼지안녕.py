from collections import deque
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
airclean = []
dust = []
for i in range(R):
    for j in range(C):
        if not arr[i][j]:
            continue
        elif arr[i][j] == -1:
            airclean.append([i, j, 0])
        elif arr[i][j]:
            dust.append([i, j, 0])

Q = deque(dust)
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for _ in range(T):
    # 미세먼지 확산
    for _ in range(len(Q)):
        v = Q.popleft()
        for i in range(4):
            w = (v[0] + dx[i], v[1] + dy[i])
            if 0 <= w[0] < R and 0 <= w[1] < C and arr[w[0]][w[1]] != -1:
                Q.append(w)
                tmp = arr[v[0]][v[1]] // 5
                visit[v[0]][v[1]] -= tmp
                visit[w[0]][w[1]] += tmp
    for i in range(R):
        for j in range(C):
            arr[i][j] += visit[i][j]
            visit[i][j] = 0

        #         v[2] += 1
        # arr[v[0]][v[1]] -= (tmp*v[2])
        # v[2] = 0

print(arr)