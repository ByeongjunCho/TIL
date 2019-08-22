# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

def paper(x, N):
    if x == N:
        return 1
    elif x > N:
        return 0
    else:
        return paper(x+10, N) + paper(x+20, N)*2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper(0, N)))