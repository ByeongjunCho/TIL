N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

s = []
def comb(start, m):
    if len(s) == 3:
        print(s)
        return

    for i in range(start, m):
        s.append(i)
        comb(i+1, m)
        s.pop()

comb(0, M)