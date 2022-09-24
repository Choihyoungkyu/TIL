import sys
sys.stdin = open('input.txt')

def f(i, j, s):
    global minV
    if i == N-1 and j == N-1:                      # 인덱스 i == 원소의 개수
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        if i+1 < N:
            f(i+1, j, s + arr[i+1][j])
        if j+1 < N:
            f(i, j+1, s + arr[i][j+1])

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * N
    f(0, 0, arr[0][0])
    print(f'#{idx} {minV}')