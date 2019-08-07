# 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open('sample_input.txt', 'r')

def cook_min(arr, N):
    cook = list(range(N))
    cook_tmp = cook[:]
    min_cook = 20000 * 16
    for i in range(N << 2):
        count = 0
        for j in range(len(arr)):
            tmp = []
            if i&(1<<j):
                tmp.append(cook_tmp[N-1-j])
                count += 1
        if count != N/2:
            continue
        tmp1 = 0
        tmp2 = 0

        for i in range(len(tmp)-1):
            for j in range(i, len(tmp)):
                tmp1 += arr[tmp[i]][tmp[j]]

        for i in range(len(tmp)):
            cook.pop(tmp[i])

        for i in range(len(cook)-1):
            for j in range(i, len(cook)):
                tmp2 += arr[cook[i]][cook[j]]
        if min_cook > abs(tmp1-tmp2):
            min_cook = abs(tmp1-tmp2)
    return min_cook

for T in range(1, int(input())+1):
    N = int(input())
    test_arr = []
    for _ in range(N):
        test_arr.append(list(map(int, input().split())))
    print('#{} {}'.format(T, cook_min(test_arr, N)))