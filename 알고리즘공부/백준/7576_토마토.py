def tototo():
    result = 0
    dy = (0, 0, -1, 1)
    dx = (1, -1, 0, 0)

    cnt = 0 # 익은 토마토의 개수
    hidden = 0 # 익지 않은 토마토의 개수
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0 or tomato[i][j] == 1:
                cnt += 1
            if tomato[i][j] == 0:
                hidden += 1
    if hidden == 0:
        return 0

    visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(M * N):
        result += 1
        tmp = []  # 익는 토마토 좌표 임시 저장
        for i in range(N):
            for j in range(M):
                if tomato[i][j] == 1:
                    tomato_all.add((i, j))
                    visit[i][j] = 1
                    for k in range(4):
                        wy, wx = dy[k] + i, dx[k] + j
                        if 0 <= wy < N and 0 <= wx < M and tomato[wy][wx] == 0 and not visit[wy][wx]:
                            tomato_all.add((wy, wx))
                            tmp.append((wy, wx))
                            visit[wy][wx] = 1
        for y, x in tmp:
            tomato[y][x] = 1
        if len(tomato_all) == cnt:
            return result
    return -1

M, N = map(int, input().split()) # M: 가로, N: 세로
tomato = [list(map(int, input().split())) for _ in range(N)]

tomato_all = set()  # 익는 토마토의 모든 좌표를 저장
result = 0  # 날짜

print(tototo())

