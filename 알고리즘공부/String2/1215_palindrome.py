import sys
sys.stdin(open('input.txt', 'r'))
def Pal(arr, M):
    # 행
    count = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])-M+1):
            for i in range(M >> 1):
                if arr[row][col+i] != arr[row][col+M-1-i]:
                    break
            else:
                count += 1
    for row in range(len(arr)-M+1):
        for col in range(len(arr[0])):
            for i in range(M >> 1):
                if arr[row+i][col] != arr[row+M-1-i][col]:
                    break
            else:
                count += 1
    return count

for T in range(1, 11):
    M = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(input()))
    print('#{} {}'.format(T, Pal(arr, M)))