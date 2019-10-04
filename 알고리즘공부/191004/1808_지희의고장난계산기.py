def backtrack(k, vals):
    if k > len(str(N)) - 1:
        return
    for i in range(len(used)):
        if k > 0 and used[i] == 0:
            continue
        backtrack(k+1, 10**k + used[i])

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    N = input()
    # 사용할 수 있는 숫자를 구한다
    used = []
    for i in range(len(arr)):
        if arr[i] == '1':
            used.append(i)