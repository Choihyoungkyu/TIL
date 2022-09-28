import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
lst = [[] for _ in range(len(arr)//2)]
for i in range(0, len(arr), 2):
    lst[arr[i]].append(arr[i+1])
    lst[arr[i+1]].append(arr[i])

def dfs(i):
    visited = [0] * (len(lst))
    stack = [0] * (len(lst))
    top = -1
    visited[i] = 1
    print(i, end=' ')
    while True:
        for j in lst[i]:
            if visited[j] == 0:
                top += 1
                stack[top] = i
                visited[j] = 1
                i = j
                print(i, end=' ')
                break
        else:
            if top != -1:
                i = stack.pop(top)
                top -= 1
            else:
                break
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
print('DFS :', end=' ')
dfs(1)
print()
print('BFS :', end=' ')
bfs(1)
