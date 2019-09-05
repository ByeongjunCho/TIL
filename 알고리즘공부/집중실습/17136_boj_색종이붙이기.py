arr = [list(map(int, input().split())) for _ in range(10)]

five = [[1 for _ in range(5)] for _ in range(5)]
four = [[1 for _ in range(4)] for _ in range(4)]
three = [[1 for _ in range(3)] for _ in range(3)]
two = [[1 for _ in range(2)] for _ in range(2)]

case = [five, four, three, two]
test_case = [5, 5, 5, 5]
for _ in range(4):
    for idx, c in enumerate(case):
        all_flag = 0
        slide = 10 - len(c) + 1
        for row in range(slide):
            for col in range(slide):
                inner_flag = 0
                if not test_case[idx]:
                    all_flag = 1
                    break
                for i in range(len(c)):
                    for j in range(len(c)):
                        if arr[row+i][col+j] != c[i][j]:
                            inner_flag = 1
                    if inner_flag == 1:
                        break
                else:
                    for i in range(len(c)):
                        for j in range(len(c)):
                            arr[row+i][col+j] = 0
                    test_case[idx] -= 1
            if all_flag:
                break
one = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            one += arr[i][j]

if one > 5:
    print(-1)
else:
    print(20 - sum(test_case) + one)