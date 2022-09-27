import sys
sys.stdin = open('input.txt')

def f(i, k, s):
    global minV
    if i == k and minV > s:
        minV = s

    elif s > minV:
        return

    else:
        for j in range(k):
            if bit[j] == 0:
                bit[j] = 1
                f(i+1, k, s+arr[i][j])
                bit[j] = 0

for idx in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    minV = 100 * N
    f(0, N, 0)
    print(f'#{idx} {minV}')