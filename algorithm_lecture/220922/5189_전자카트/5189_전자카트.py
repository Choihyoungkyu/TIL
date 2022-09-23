import sys
sys.stdin = open('input.txt')

def f(i, k, s):
    global minV
    global index
    if i == k:
        if s < minV:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(N):
            if index and i == index and j == 0:
                continue
            if p[j] != -1 and arr[i][j] != 0:
                p[j] = -1
                if i == 0:
                    index = j
                f(i+1, k, s+arr[i][j])
                p[j] = j

for idx in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N * 100
    index = 0
    f(0, N, 0)
    print(f'#{idx} {minV}')

