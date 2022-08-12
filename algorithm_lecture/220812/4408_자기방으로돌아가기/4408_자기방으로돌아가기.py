import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    room = [0] * 200
    for i in range(N):
        if lst[i][0] % 2 == 1:
            x = (lst[i][0]+1) // 2
        else:
            x = lst[i][0] // 2

        if lst[i][1] % 2 == 1:
            y = (lst[i][1] + 1) // 2
        else:
            y = lst[i][1] // 2

        if x < y:
            for j in range(x-1, y):
                room[j] += 1
        else:
            for j in range(y-1, x):
                room[j] += 1
    print(f'#{idx} {max(room)}')