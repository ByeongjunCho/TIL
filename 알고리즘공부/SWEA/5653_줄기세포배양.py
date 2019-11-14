# 5653. [모의 SW 역량테스트] 줄기세포배양

for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())  # 행, 열, 시간
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 좌표를 dict 에 입력

    cell = {}
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cell.update({(i, j): [arr[i][j], -arr[i][j]]})  # 행렬값, 활성화여부

    def clone():
        dy = [0, 0, -1, 1]
        dx = [1, -1, 0, 0]
        keys = set(cell.keys())
        for k in keys:
            val = cell[k]
            # 활성화된 것이 아니라면
            if 0 > val[1]:
                cell.update({k: [val[0], val[1] + 1]})
            # 활성화된 세포라면
            elif 0 <= val[1] < val[0]:
                cell.update({k: [val[0], val[1] + 1]})
                for i in range(4):
                    wy, wx = dy[i] + k[0], dx[i] + k[1]
                    # 기존에 있는 셀이 금방 복사된 것이면서 생명력이 작다면
                    if (wy, wx) not in keys and cell.get((wy, wx)) and cell.get((wy, wx))[0] == -cell.get((wy, wx))[1] and cell.get((wy, wx))[0] < val[0]:
                        cell.update({(wy, wx): [val[0], -val[0]]})
                    # 복사하려는 자리에 cell이 없다면
                    elif not cell.get((wy, wx)):
                        cell.update({(wy, wx): [val[0], -val[0]]})
                    # 복사하려는 자리의 생명력이 넣을 값보다 크다면
                    # elif cell.get((wy, wx)) and cell.get((wy, wx))[0] == -cell.get((wy, wx))[1] and cell.get((wy, wx))[0] >= val[0]:
                    #     continue
                    # 이미 자리를 차지한 값이면서 최근것이 아니면
                    # elif cell.get((wy, wx)) and cell.get((wy, wx))[0] > cell.get((wy, wx))[1]:
                    #     continue

    for _ in range(K):
        clone()

    # print(cell)
    count = 0
    for val in cell.values():
        if val[0] > val[1]:
            count += 1

    print('#{} {}'.format(tc, count))