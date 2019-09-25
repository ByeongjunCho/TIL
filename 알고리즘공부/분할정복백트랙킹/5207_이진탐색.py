def binarySearch(lo, hi, target):
    start = lo
    stop = hi
    flag = 0
    while start < stop:
        mid = (start+stop) >> 1

        if tar[mid] == target:
            return 1

        if tar[mid] < target:
            start = mid+1
            if not flag:
                flag = 1
            else:
                return 0
        else:
            stop = mid
            if flag:
                flag = 0
            else:
                return 0

        if start == stop:
            break
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tar = list(map(int, input().split()))
    dst = list(map(int, input().split()))
    result = 0
    for i in range(M):
        result += binarySearch(0, N, dst[i])
    print('#{} {}'.format(tc, result))

