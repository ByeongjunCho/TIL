from collections import deque
def BFS(dst, tar):
    Q = deque()
    Q.append(dst)
    result = 0
    while Q:
        result += 1
        v = Q.popleft()
        w = v+1
        if w == tar:
            return result
        Q.append(w)
        w = v-1
        if w == tar:
            return result
        Q.append(w)
        w = v*2
        if w == tar:
            return result
        Q.append(w)

N, K = map(int, input().split())
print(BFS(N, K))