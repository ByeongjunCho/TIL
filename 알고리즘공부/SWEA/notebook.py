# def find_max_index(values):
#     max_value = 0
#     for i in range(len(values) - 1):
#         if max_value >= values[i]:
#             return i
#         elif values[i] < values[i+1]:
#             max_value = values[i]
#         else:
#             return i
#     else:
#         return i + 1

# l1 = [1, 1, 3, 1, 2]  
# print(find_max_index(l1))


test_case = int(input())
test_list = []
for i in range(1, test_case + 1):
    result = 0
    tmp = input()
    test_list = tmp.split()
    test_list.sort(key=int)
    for n in test_list[1:9]:
        result += int(n)
    print(f'#{i} {round(result/8)}')