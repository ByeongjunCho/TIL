# 어디에 단어가 들어갈 수 있을까
def conv_count(tar, tar_size, dst): # 입력이 2중 리스트라 가정
    count = 0
    for height in range(tar_size):
        result = 0
        for width in range(tar_size):
            result += tar[height][width]
        if result == dst:
            count += 1
    
    for width in range(tar_size):
        result = 0
        for height in range(tar_size):
            result += tar[width][height]
        if result == dst:
            count += 1
    



test_case = int(input())

for case in range(1, test_case + 1):
    test_arr = []
    target_size, window_size = map(int, input().split())
    for _ in range(target_size):
        test_arr.append(list(map(int, input().split())))
    
    print(f'#{case} {conv_count(test_arr, target_size, window_size)}')