# 1267. [S/W 문제해결 응용] 10일차 - 작업순서

import sys
sys.stdin = open('1267_input.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    caseE = list(map(int, input().split()))
    for i in range(E):
        G[caseE[i << 1]].append(caseE[(i << 1)+1])
    visit = [False] * (V+1)
    # 전처리

    start_case = []

    output_count = list(map(len, G))
    # for i in range(len(output_count)):
    #     if not output_count[i]:
    #         output_count[i] = 1

    for i in range(1, V+1):
        for k in G:
            if i in k:
                break
        else:
            start_case.append(i)
    input_count = []
    for j in range(0, V+1):
        count = 0
        for k in G:
            if j in k:
                count += 1
        input_count.append(count)

    print(G)
    print(start_case)
    print(input_count)
    print(output_count)

    result = ''
    v = start_case.pop()
    visit[v] = True
    tmp_visit = []
    S = [v]
    signal = 0
    while start_case and S:
        for w in G[v]:
            if not visit[w]:
                #
                #     continue
                if input_count[w] > 1:
                    visit[w] = True
                    tmp_visit.append(w)
                    v = S.pop()
                    input_count[w] -= 1
                    continue

                print('{} -> {}'.format(v, w))
                visit[w] = True
                S.append(w)
                v = w
                break
        else:
            if not S:
                v = start_case.pop()
                S = [v]
                for val in tmp_visit:
                    visit[val] = not visit[val]
            else:
                v = S.pop()
                for val in tmp_visit:
                    visit[val] = not visit[val]





