# 1216. [S/W 문제해결 기본] 3일차 - 회문2
import sys
sys.stdin = open('1216.txt', 'r')

def Pal(arr):

    for case in range(100, 0, -1):
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                # 열 슬라이딩
                if col <= (len(arr) - case):
                    for i in range(case >> 1):
                        if arr[row][col+i] != arr[row][col+case-1-i]:
                            break
                    else:
                        return case
                # 행 슬라이딩
                if row <= (len(arr) - case):
                    for i in range(case >> 1):
                        if arr[row+i][col] != arr[row+case-1-i][col]:
                            break
                    else:
                        return case
    return 1

for _ in range(10):
    T = input()
    arr = []
    for _ in range(100):
        arr.append(list(input()))
    print('#{} {}'.format(T, Pal(arr)))