# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

def DelReAlpah(string):
    status = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            status = 1
            string = string[:i] + string[i+2:]
            break
    if not status:
        return string
    else:
        return DelReAlpah(string)

T = int(input())

for tc in range(1, T+1):
    test_string = input()
    result = DelReAlpah(test_string)
    if not result:
        result = 0
    else:
        result = len(result)
    print('#{} {}'.format(tc, result))
