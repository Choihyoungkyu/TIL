import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    que = [[x, y]]
    visited[x][y] = 0
    while que:
        nx, ny = que.pop(0)
        for di, dj in D:
            ni, nj = nx+di, ny+dj
            if 0<=ni<N and 0<=nj<N:
                if lst[ni][nj] - lst[nx][ny] > 0:           # 올라갈 때만 추가 연료가 필요하므로
                    height = lst[ni][nj] - lst[nx][ny]
                else:
                    height = 0
                # 방문을 안했거나 연료가 더 적게 드는 경우
                if visited[ni][nj] == -1 or visited[ni][nj] > visited[nx][ny] + 1 + height:
                    que.append([ni, nj])
                    visited[ni][nj] = visited[nx][ny] + 1 + height

D = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하우상좌

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc} {visited[N-1][N-1]}')

    for i in visited:
        print(*i)
    print()

