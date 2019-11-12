# 4008. [모의 SW 역량테스트] 숫자 만들기

for tc in range(1, int(input()) + 1):
    N = int(input())
    calc = list(map(int, input().split()))
    operator = []
    # 계산자 만들기
    operator += ['+'] * calc[0]
    operator += ['-'] * calc[1]
    operator += ['*'] * calc[2]
    operator += ['/'] * calc[3]

    numbers = list(map(int, input().split()))
    def calculator(numbers, operators):
        tmp = numbers[0]

        for i in range(1, len(numbers)):
            if operators[i-1] == '+':
                tmp += numbers[i]
            elif operators[i-1] == '-':
                tmp -= numbers[i]
            elif operators[i-1] == '*':
                tmp *= numbers[i]
            elif operators[i-1] == '/':
                tmp = int(tmp / numbers[i])

        return tmp


    mymax = -10e10
    mymin = 10e10

    def perm(k):
        if k == len(operator):
            global mymax
            global mymin
            tmp = calculator(numbers, operator)
            mymax = max(mymax, tmp)
            mymin = min(mymin, tmp)
            return
        for i in range(k, len(operator)):
            operator[k], operator[i] = operator[i], operator[k]
            perm(k+1)
            operator[k], operator[i] = operator[i], operator[k]

    perm(0)
    print('#{} {}'.format(tc, mymax - mymin))