import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        cnt_x = 0
        cnt_y = 0
        for j in range(N):
            if arr[i][j] == 1:                       # 행 탐색
                cnt_x += 1
                if j == N-1 and cnt_x == K:
                    cnt += 1
                    cnt_x = 0
            else:
                if cnt_x == K:
                    cnt += 1
                cnt_x = 0

            if arr[j][i] == 1:                      # 열 탐색
                cnt_y += 1
                if j == N-1 and cnt_y == K:
                    cnt += 1
                    cnt_y = 0
            else:
                if cnt_y == K:
                    cnt += 1
                cnt_y = 0

    print(f'#{idx} {cnt}')

