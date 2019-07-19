import csv
audiAcc = []  # 영화코드 리스트
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    boxoffice = csv.reader(f)
    i = 0  # 첫줄은 출력하지 않도록 하자.
    for line in boxoffice:
        if i > 0 and i % 2 == 0:
            print(line)
            audiAcc.append(line[0])
            
        i += 1
print(audiAcc)

# import csv
# audiAcc = []  # 영화코드 리스트
# with open('boxoffice.csv', 'r', encoding='utf-8') as f:
#     boxoffice = csv.reader(f)
#     # i = 0  # 첫줄은 출력하지 않도록 하자.
#     for line in boxoffice:
#         # if i > 0 and i % 2 == 0:
#         print(line)
#             # audiAcc.append(line[0])
#             # i += 1
       
# print(audiAcc)