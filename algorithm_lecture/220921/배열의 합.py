
def f(i, k, s):
    global minV
    if i == k:                      # 인덱스 i == 원소의 개수
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N * 10
    f(0, N, 0)
    print(f'#{idx} {minV}')
