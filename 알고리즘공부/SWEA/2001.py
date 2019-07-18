# 파리 퇴치

arr = [[1, 3, 3, 6, 7],[8, 13, 9, 12, 8],[4, 16, 11, 12, 6],
[2, 4, 1, 23, 2],[9, 13, 4, 7, 3]]

window = [[1, 1],[1, 1]]


def conv_max(tar, win):
    tar_w, tar_h = len(tar[0]), len(tar)
    win_w, win_h = len(win[0]), len(win)

    slide_w = tar_w - win_w + 1
    slide_h = tar_h - win_h + 1
     
    aa = []
    for h in range(slide_h):
        for w in range(slide_w):
            result = 0
            for j in range(win_h):
                for i in range(win_w):
                    result += win[j][i] * tar[h+j][w+i]

            else:
                aa.append(result)
    return aa
print(len(conv_max(arr, window)))

