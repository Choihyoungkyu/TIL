import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    for p in range(2*N-1):
        cnt = 1
        x = 1
        y = 1
        if p % 2 == 0:
            if x % 2 == 1:
                for j in range(N-p):
                    arr[][j] = cnt
                    cnt += 1
                    x += 1
            else:
                for j in range(N-x+1, -1):
                    arr[N-x/2][j]
                    cnt += 1
                    x += 1

