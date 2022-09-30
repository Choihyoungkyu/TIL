# BFS
import sys
sys.stdin = open('input.txt')

D = [[1, 0], [0, 1], [-1, 0], [0, -1]]      # 하우상좌

def bfs(i, j):
    que = [[i, j]]
    visited[i][j] = 0
    while que:
        ni, nj = que.pop(0)
        for di, dj in D:
            y, x = ni + di, nj + dj
            if 0<=y<N and 0<=x<N and (visited[y][x]==-1 or visited[y][x] > visited[ni][nj] + lst[y][x]):
                visited[y][x] = visited[ni][nj] + lst[y][x]
                que.append([y, x])

for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc} {visited[N-1][N-1]}')