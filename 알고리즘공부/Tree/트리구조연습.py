G = [[], [2,3,4], [5], [], [6], [], []]
value = [0, 30, 54, 2, 45, 1, 123]

def dfs(n):
    print(value[n], end=' ')
    for v in G[n]:
        dfs(v)
    print()

dfs(1)