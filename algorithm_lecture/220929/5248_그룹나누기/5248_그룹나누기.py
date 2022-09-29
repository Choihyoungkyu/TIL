import sys
sys.stdin = open('input.txt')

def bfs(n):
    global cnt
    cnt += 1
    que = [n]
    visited[n] = 1
    while que:
        t = que.pop(0)
        for k in dic[t]:
            if visited[k] == 0:
                que.append(k)
                visited[k] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {i:[] for i in range(1, N+1)}
    for i in range(0, 2*M, 2):
        dic[lst[i]].append(lst[i+1])
        dic[lst[i+1]].append(lst[i])
    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
    print(f'#{tc} {cnt}')