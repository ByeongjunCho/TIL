# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
import sys
sys.stdin = open('1210_input.txt', 'r')

# for _ in range(1, 11):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     row = 99
#     idx = arr[row].index(2)
#     while row != 0:
#         if idx == 0 and not arr[row][idx+1]:
#             row -= 1
#
#         elif idx == 99 and not arr[row][idx-1]:
#             row -= 1
#
#         elif (idx > 0 and not arr[row][idx-1]) and (idx < 99 and not arr[row][idx+1]):
#             row -= 1
#
#
#         else:
#             if idx > 0 and arr[row][idx-1]:
#                 while arr[row][idx] and idx > -1 :
#                     idx -= 1
#                 row -= 1
#                 idx += 1
#             elif idx < 99 and arr[row][idx+1]:
#                 while idx < 100 and arr[row][idx] :
#                     idx += 1
#                 row -= 1
#                 idx -= 1
#     print('#{} {}'.format(T, idx))

# rowcol = [[0 for _ in range(100)] for _ in range(100)]
def ladder1(arr, row, idx):
    if row == 0:
        return idx
    if idx == 0 and not arr[row][idx+1]:
        return ladder1(arr, row-1, idx)

    elif idx == 99 and not arr[row][idx - 1]:
        return ladder1(arr, row-1, idx)

    elif (idx > 0 and not arr[row][idx - 1]) and (idx < 99 and not arr[row][idx + 1]):
        return ladder1(arr, row-1, idx)
    else:
        if idx > 0 and arr[row][idx-1]:
            while arr[row][idx] and idx > -1:
                idx -= 1
            row -= 1
            idx += 1
        elif idx < 99 and arr[row][idx+1]:
            while idx < 100 and arr[row][idx]:
                idx += 1
            row -= 1
            idx -= 1

        return ladder1(arr, row, idx)

# for _ in range(1, 11):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     row = 99
#     idx = arr[row].index(2)
#
#     print('#{} {}'.format(T, idx))

for _ in range(1, 11):
    T = input()
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    row = 99
    idx = arr[row].index(2)

    print('#{} {}'.format(T, ladder1(arr, row, idx)))