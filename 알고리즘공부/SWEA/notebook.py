s = []
N = 3
W = 6

def start(k):
    if k == N:
        print(s)
        return

    for i in range(W):
        s.append(i)
        start(k + 1)
        s.pop()

start(0)