# 기울이는 함수
def go(row, col, color, status):
    # status == 1 : 위
    if status == 1:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= i-1 < N and arr[i - 1][j] == 'O':
                return (i-1, j)
            elif 0 <= i-1 < N and arr[i - 1][j] == '.':
                i -= 1
            else:
                break
        arr[i][j] = color
    # status == 2: 오
    elif status == 2:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= j+1 < M and arr[i][j+1] == 'O':
                return (i, j+1)
            elif 0 <= j+1 < M and arr[i][j+1] == '.':
                j += 1
            else:
                break
        arr[i][j] = color
    # status == 3: 아
    elif status == 3:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= i+1 < N and arr[i + 1][j] == 'O':
                return (i+1, j)
            elif 0 <= i+1 < N and arr[i + 1][j] == '.':
                i += 1
            else:
                break
        arr[i][j] = color
    # status == 4: 왼
    else:
        i, j = row, col
        arr[i][j] = '.'
        while True:
            if 0 <= j-1 < M and arr[i][j-1] == 'O':
                return (i, j-1)
            elif 0 <= j-1 < M and arr[i][j-1] == '.':
                j -= 1
            else:
                break
        arr[i][j] = color
    return (i, j)

def ball(red, blue, status): # 1234=>위오아왼
    if status == 1: # 위
        if red[0] > blue[0]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    elif status == 2: # 오
        if red[1] < blue[1]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    elif status == 3: # 아
        if red[0] < blue[0]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b
    else:
        if red[1] > blue[1]:
            b = go(blue[0], blue[1], 'B', status)
            r = go(red[0], red[1], 'R', status)
            return r, b
        else:
            r = go(red[0], red[1], 'R', status)
            b = go(blue[0], blue[1], 'B', status)
            return r, b

N, M = map(int, (input().split()))
arr = [list(input()) for _ in range(N)]

# 파라미터 좌표

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red = (i, j)
        elif arr[i][j] == 'B':
            blue = (i, j)
        elif arr[i][j] == 'O':
            hole = (i, j)

def play(k, br, bb, ar, ab):

    for status in range(1, 5):
        r, b = ball(br, bb, status)
        play(k+1, )