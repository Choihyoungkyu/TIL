import sys
sys.stdin = open('input.txt')

def f(i, k, s, r):
    global maxV, order
    if i == k:
        if s <= C and maxV < s:
            maxV = s
            order = r
    elif s > C:
        return
    else:
        for j in range(i, k):
            if bit[j] == 0:
                bit[j] = 1
                f(i+1, k, s+lst[i], r+str(1))
                bit[j] = 0
                f(i+1, k, s, r+str(0))

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    candidates = {}
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            lst = arr[i][j:j+M]
            bit = [0] * M
            maxV = 0
            order = ''
            f(0, M, 0, '')
            visited[i][j] = maxV
            try:
                candidates[maxV].append((i, j, order))
            except:
                candidates[maxV] = [(i, j, order)]
        for j in range(N-M+1, N):
            lst = arr[i][j:N]
            bit = [0] * (N-j)
            maxV = 0
            order = ''
            f(0, N-j, 0, '')
            visited[i][j] = maxV
            try:
                candidates[maxV].append((i, j, order))
            except:
                candidates[maxV] = [(i, j, order)]

    dec = sorted(candidates, reverse=True)
    # print(dec)
    for i in dec:
        candidates[i].sort(key=lambda x:x[2].count('1'))
    print(candidates)
    # for i in visited:
    #     print(*i)
    # print()

    i1, j1, r1 = candidates[dec[0]].pop(0)
    flag = False
    for idx in dec:
        print(idx, end=' ')
        while candidates[idx]:
            i2, j2, r2 = candidates[idx].pop(0)
            if i1 != i2 or j2 - j1 > M-1:
                flag = True
                break
        if flag:
            break
    print()
    print(f'{[i1, j1, r1]}, {[i2, j2, r2]}')

    # for i in arr:
    #     print(*i)
    # print()
    res = 0
    bit = [0] * M
    maxV = 0
    order = ''
    lst = arr[i1][j1:j1+len(r1)]

    f(0, len(r1), 0, '')
    for i in range(len(r1)):
        if r1[i] == '1':
            print(lst[i], end=' ')
            res += lst[i] ** 2

    bit = [0] * M
    maxV = 0
    order = ''
    lst = arr[i2][j2:j2+len(r2)]

    f(0, len(r2), 0, '')
    for i in range(len(r2)):
        if r2[i] == '1':
            print(lst[i], end=' ')
            res += lst[i] ** 2
    print()
    print(f'#{tc} {res}')
    print()