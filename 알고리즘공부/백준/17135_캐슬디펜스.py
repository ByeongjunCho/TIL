from copy import deepcopy
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
copy_arr = deepcopy(arr)
def kill(arc, d):
    row, col = len(copy_arr), len(copy_arr[0])
    for dist in range(d):
        start = [row-dist, arc-d]
        stats = 1
        while True:
            if 0 > start[0] or start[1] > col-1 or start[1] < 0:
                start = [start[0] - stats, start[1] + 1]
                if start[0] > row - 1:
                    break
                elif start[1] == arc:
                    stats = -1
                continue
            elif copy_arr[start[0]][start[1]] == 1:
                copy_arr[start[0]][start[1]] = 0
                return 1
            else:
                start = [start[0] - stats, start[1] + 1]
                if start[0] > row-1:
                    break
                elif start[1] == arc:
                    stats = -1
    return 0



# s = []
# def comb(start, m):
#     if len(s) == 3:
#
#         return
#
#     for i in range(start, m):
#         s.append(i)
#         comb(i+1, m)
#         s.pop()
#
# comb(0, M)
kill(0, 2)
print(copy_arr)