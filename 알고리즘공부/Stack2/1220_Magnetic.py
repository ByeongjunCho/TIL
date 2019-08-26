# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
import sys
sys.stdin = open('1220_input.txt', 'r')

for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N극 1/S극 2 위가 N극 아래 S극
    for col in range(N):
        for _ in range(100):
            for row in range(N):
                # S자성채의 경우
                if arr[row][col] == 2:  # S극 자성체(위로) 0 1 2 3 ...
                    if row == 0:
                        arr[row][col] = 0
                    # 위에 값이 없는 경우
                    elif not (arr[row-1][col]):
                        arr[row][col], arr[row-1][col] = arr[row-1][col], arr[row][col]

                # N자성체
                if arr[N-1-row][col] == 1: # N극 자성체(아래로) 99 98 97 ...
                    if row == 0:
                        arr[N-1-row][col] = 0

                    # 아래에 값이 없는 경우
                    elif not (arr[N-1-row-1][col]):
                        arr[N-1-row][col], arr[N-1-row+1][col] = arr[N-1-row+1][col], arr[N-1-row][col]
    tmp = 0
    S = 0
    for col in range(N):
        for row in range(N-1):
            if arr[row][col] == 1 and arr[row+1][col] == 2:
                tmp += 1

    print('#{} {}'.format(tc, tmp))
# for i in range(N):
#     print(arr[i][0])




