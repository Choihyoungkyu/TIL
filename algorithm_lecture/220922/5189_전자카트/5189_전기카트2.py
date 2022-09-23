import sys
sys.stdin = open('input.txt')

def f(i, k, index, s):
    global minV
    if i == k:
        s += arr[index][0]
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(N):
            if p[j] != -1:
                p[j] = -1
                f(i+1, k, j, s+arr[index][j])
                p[j] = j

for idx in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    p[0] = -1
    minV = N * 100
    lst = []
    f(1, N, 0, 0)
    print(f'#{idx} {minV}')

