
def password(k, L, C, s):
    if k == L:
        print(s)
        return
    for i in range(k, L+k-1):
        if alpabet[i] in s:
            continue
        password(k+1, L, C, s+alpabet[i])

L, C = map(int, input().split())
alpabet = input().split()



alpabet.sort()
password(0, L, C, '')