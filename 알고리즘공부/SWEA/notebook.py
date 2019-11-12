def makefilter(K):
    N = 2*(K-1) + 1
    count = 0
    vec2 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N//2):
        count = 2*i + 1
        for j in range(K-i-1, N):
            vec2[i][j] = 1
            count -= 1
            if not count:
                break
    c = N
    for i in range(N//2, N):
        count = c
        for j in range(i-K+1, N):
            vec2[i][j] = 1
            count -= 1
            if not count:
                break
        c -= 2
    return vec2

arr = makefilter(5)
for a in arr:
    print(a)