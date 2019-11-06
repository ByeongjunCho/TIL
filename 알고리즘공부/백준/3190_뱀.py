from collections import deque
N = int(input())
K = int(input()) # 사과의 수
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 3 # 사과

snake = deque()
snake.append([0, 0])
def go(status): # 0123
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # head 추출
    i, j = snake.popleft()
    wy = i + dy[status]
    wx = j + dx[status]
    if 0 <= wy < N and 0 <= wx < N:
        if [wy, wx] in snake:
            return False
        else:
            snake.appendleft([wy, wx])
    else:
        return False
    # 머리에 사과가 없다면 꼬리 제거
    if arr[wy][wx] != 3:
        snake.pop()
    return True

