# def freedom(k, N, cnt, day):
#     global result
#     for i in range(k+day, N):
#         freedom(i, N, cnt + P[i], T[i])
#         print(cnt)
#         result = max(cnt, result)
#
# N = int(input())
# T = []
# P = []
# for _ in range(N):
#     d, p = map(int, input().split())
#     T.append(d)
#     P.append(p)
#
#
# for i in range(N-1, -1, -1):
#     if T[i] + i > N:
#         T.pop()
#         P.pop()
#     else:
#         break
#
#
# result = 0
# freedom(0, len(T), 0, 0)
# print(result)


def freedom(k, N, cnt, day):
    global result
    if k == N:
        result = max(cnt, result)
        return
    day -= 1
    for i in range(k, N):
        if day > 0:
            day -= 1
            continue
        freedom(i+1, N, cnt + P[i], T[i])


N = int(input())
T = []
P = []
for _ in range(N):
    d, p = map(int, input().split())
    T.append(d)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i] + i > N:
        T.pop()
        P.pop()
    else:
        break
result = 0
freedom(0, len(T), 0, 0)
print(result)