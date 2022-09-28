import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
lst = [[] for _ in range(len(arr)//2)]
for i in range(0, len(arr), 2):
    lst[arr[i]].append(arr[i+1])
    lst[arr[i+1]].append(arr[i])

def bfs(n):
    visited = [0] * (len(arr))
    q = [n]
    visited[n] = 1
    print(n, end=' ')
    while q:
        t = q.pop(0)
        for i in lst[t]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = 1
                q.append(i)
bfs(1)