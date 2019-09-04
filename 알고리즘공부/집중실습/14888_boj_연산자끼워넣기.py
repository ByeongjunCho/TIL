N = int(input())
numbers = list(map(int, input().split()))
cs = list(map(int, input().split()))  # +, -, *, /

mymax = -1000000001
mymin = 1000000001
def calc(k, N, result):
    global mymax
    global mymin
    if k == N:
        mymax = max(mymax, result)
        mymin = min(mymin, result)
    if cs[0]:
        cs[0] -= 1
        calc(k+1, N, result+numbers[k])
        cs[0] += 1
    if cs[1]:
        cs[1] -= 1
        calc(k + 1, N, result - numbers[k])
        cs[1] += 1
    if cs[2]:
        cs[2] -= 1
        calc(k + 1, N, result * numbers[k])
        cs[2] += 1
    if cs[3]:
        cs[3] -= 1
        if result < 0:
            calc(k + 1, N, -(abs(result) // numbers[k]))
        else:
            calc(k + 1, N, result // numbers[k])
        cs[3] += 1


calc(1, N, numbers[0])

print(mymax)
print(mymin)