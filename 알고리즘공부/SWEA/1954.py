# 달팽이 숫자
def snail(size):
    result = [[0]*size] * size
    row, col = 0, 0
    tmp = 1
    count = 1
    while True:
        # 가로를 채운다
        for w in range(row, size, tmp):
            result[row][w] = count
            count+=1