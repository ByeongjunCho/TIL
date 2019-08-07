# 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open('sample_input.txt', 'r')

def cook_min(arr, N):
    min_cook = 20000 * 16
    for i in range(2**N):
        cook = list(range(N))
        cook_tmp = cook[:]
        tmp1 = 0  
        tmp2 = 0
        tmp = []
        for j in range(len(arr)):
            if i&(1<<j):
                tmp.append(cook_tmp[N-1-j])
        # tmp = [cook_tmp[N-1-x] for x in range(len(arr)) if i&(1<<x)]
                
        if len(tmp) != N/2:
            continue
        
        else:

            for i in range(len(tmp)):
                cook.pop(tmp[i])

            for i in range(len(cook)):
                for j in range(len(cook)):
                    tmp1 += arr[tmp[i]][tmp[j]]
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