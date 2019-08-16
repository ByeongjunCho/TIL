# 4408. 자기 방으로 돌아가기

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     student_num = int(input())
#     room = [0] * 200
#
#     for _ in range(student_num):
#         recent_room, target_room = map(int, input().split())
#         for i in range(recent_room, target_room+1):
#             room[i] += 1
#
#     print('#{} {}'.format(test_case, max(room)))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    student_num = int(input())
    room = [0] * 200

    for _ in range(student_num):
        recent_room, target_room = map(int, input().split())
        recent_room = round((recent_room / 2 - 0.6))
        target_room = round((target_room / 2 - 0.6))
        if recent_room <= target_room:
            for i in range(recent_room, target_room+1):
                room[i] += 1
        else:
            for j in range(target_room, recent_room-1, -1):
                room[j] += 1

    print('#{} {}'.format(test_case, max(room)))