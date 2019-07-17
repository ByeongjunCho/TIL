# 백만장자 프로젝트
# test_case = int(input())
test_case = 1
# N = '5'
price = '3 5 9'
def find_max_index(values):
    max_value = 0
    for i in range(len(values) - 1):
        if max_value >= values[i]:
            return i
        elif values[i] >= values[i+1]:
            continue
        else:
            return i + 1
    else:
        return i

for case in range(test_case):
    # N = input()
    price = list(map(int, price.split(' ')))
    # price = list(map(int, input().split(' ')))
    len_price = len(price)

    loc = 0  # 위치변수
    get_price = 0  # 이득
    while True:
        # 1. 가장 큰 값이 있는 인덱스를 찾는다.
        if loc == len_price or loc == len_price - 1: 
            break
        max_index = find_max_index(price[loc:])
        # max_index = price[loc:].index(max(price[loc:]))

        # 2. 인덱스 값이 현재 저장된 loc와 같은지 확인해서 같다면 다음부터 다시 시작한다..
        
        if max_index == loc:
            loc += 1
        else:
            get_price += max_index * price[loc:loc + max_index + 1][-1] - sum(price[loc:loc + max_index])
            loc += max_index + 1
        
    print(f'#{case + 1} {max(get_price, 0)}')