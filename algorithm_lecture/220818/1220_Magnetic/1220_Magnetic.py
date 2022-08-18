#
import sys
sys.stdin = open('input.txt')

for idx in range(10):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 1이면 N극(빨강), 2이면 S극(파랑)
    # 아래쪽이 S극, 위쪽이 N극
    tot = 0
    for j in range(N):
        cnt_1 = cnt_2 = 0

        y_2 = 0
        for i in range(N-1, -1, -1):
            if y_2 < i and lst[i][j] == 2:
                y_2 = i
                break

        for i in range(N-1, -1, -1):
            if lst[i][j] == 1:
                y_1 = i
                if y_1 < y_2:
                    cnt_1 += 1

        y_1 = N-1
        for i in range(N):
            if y_1 > i and lst[i][j] == 1:
                y_1 = i
                break

        for i in range(N):
            if lst[i][j] == 2:
                y_2 = i
                if y_1 < y_2:
                    cnt_2 += 1
        tot += min(cnt_1, cnt_2)

    print(f'#{idx} {tot}')