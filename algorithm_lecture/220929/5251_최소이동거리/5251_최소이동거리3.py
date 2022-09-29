# DFS
import sys
sys.stdin = open('input.txt')

def dfs(n):
    stack = [0] * (N+1)
    visited[n] = 0
    top = -1
    while True:
        for i, w in adjL[n]:
            if visited[i] == -1 or visited[i] > visited[n] + w:
                top += 1
                stack[top] = n
                visited[i] = visited[n] + w
                n = i
                break
        else:
            if top != -1:
                n = stack[top]
                top -= 1
            else:
                break

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjL = {i : [] for i in range(N+1)}
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjL[u].append([v, w])
    visited = [-1] * (N + 1)
    dfs(0)
    print(f'#{tc} {visited[-1]}')