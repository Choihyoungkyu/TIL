import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 1
    cnt = 1
    i = 0
    j = 0
    ni = 0
    nj = 0
    while cnt <= N*N:
        if k % 4 == 1:
            if arr[i][j] == 0:
                arr[i][j] = cnt
                j += 1
                cnt += 1
                if j == N or arr[i][j] != 0:
                    j -= 1
                    k += 1
            else:
                j += 1
        if k % 4 == 3:
            if arr[i][j] == 0:
                arr[i][j] = cnt
                j -= 1
                cnt += 1
                if j == -1 or arr[i][j] != 0:
                    j += 1
                    k += 1
            else:
                j -= 1
        if k % 4 == 2:
            if arr[i][j] == 0:
                arr[i][j] = cnt
                i += 1
                cnt += 1
                if i == N or arr[i][j] != 0:
                    i -= 1
                    k += 1
            else:
                i += 1
        if k % 4 == 0:
            if arr[i][j] == 0:
                arr[i][j] = cnt
                i -= 1
                cnt += 1
                if i == N or arr[i][j] != 0:
                    i += 1
                    k += 1
            else:
                i -= 1
    print(f'#{idx}')
    for i in arr:
        print(*i)
