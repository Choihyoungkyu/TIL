import sys
sys.stdin = open('input.txt')

def f(i, k, s, r):                              # 순열 만들기
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
    # 각 자리별 꿀단지 최대를 visited에 저장
    for i in range(N):
        for j in range(N-M+1):
            lst = arr[i][j:j+M]
            bit = [0] * M
            maxV = 0
            tmp = 0
            order = ''
            f(0, M, 0, '')
            for k in range(len(order)):
                if order[k] == '1':
                    tmp += lst[k]**2
            visited[i][j] = tmp

        for j in range(N-M+1, N):
            lst = arr[i][j:N]
            bit = [0] * (N-j)
            maxV = 0
            tmp = 0
            order = ''
            f(0, N-j, 0, '')
            for k in range(len(order)):
                if order[k] == '1':
                    tmp += lst[k]**2
            visited[i][j] = tmp

    # for i in visited:
    #     print(*i)
    # print()
    row = []
    col = []
    for i in range(N):
        # column 부분 중 최대값
        col.append(max(visited[i]))
        maxV = 0
        # row 부분 중 최대값 -> 브루트포스
        for j in range(N-M+1):
            for k in range(j+M, N):
                if maxV < visited[i][j] + visited[i][k]:
                    maxV = visited[i][j] + visited[i][k]
        row.append(maxV)
    col.sort(reverse=True)
    row += [col[0]+col[1]]
    res = max(row)
    print(f'#{tc} {res}')