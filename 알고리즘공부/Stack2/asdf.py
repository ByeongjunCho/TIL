# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
# import sys
# sys.stdin = open('1267_input.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    caseE = list(map(int, input().split()))
    for i in range(E):
        G[caseE[i << 1]].append(caseE[(i << 1)+1])
    visit = [0] * (V+1)

    start_case = []
    for i in range(1, V+1):
        for k in G:
            if i in k:
                break
        else:
            start_case.append(i)

    input_count = []
    for j in range(0, V + 1):
        count = 0
        for k in G:
            if j in k:
                count += 1
        input_count.append(count)

    result = ''
    v = start_case.pop()
    visit[v] = 1
    S = [v]

    while S:
        for w in G[v]:
            if visit[w] + 1 == input_count[w]:
                print('{} -> {}'.format(v, w))
                visit[w] += 1
                S.append(w)
                v = w
                break
            else:
                visit[w] += 1
                v = S.pop()
                continue

        else:
            if S:
                v = S.pop()


        # if not S:
        #     v = start_case.pop()
        #     S = [v]




