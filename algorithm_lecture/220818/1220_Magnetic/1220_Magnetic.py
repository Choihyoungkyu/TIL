# 0.24229s
import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 1이면 N극(빨강), 2이면 S극(파랑)
    # 아래쪽이 S극, 위쪽이 N극
    tot = 0
    for j in range(N):
        lst_2 = []
        for i in range(N):
            if lst[i][j] == 1 or lst[i][j] == 2:
                lst_2.append(lst[i][j])
        while True:
            if lst_2[0] == 2:
                lst_2.pop(0)
            elif lst_2[-1] == 1:
                lst_2.pop()
            else:
                break

        for k in range(len(lst_2)-1):
            if lst_2[k] == 1 and lst_2[k+1] == 2:
                tot += 1

    print(f'#{idx} {tot}')