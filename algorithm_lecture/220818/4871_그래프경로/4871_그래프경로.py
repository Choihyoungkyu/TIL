# 0.12989s
import sys
sys.stdin = open('input.txt')

def dfs(S, G, lst):
    S -= 1
    G -= 1
    visited = [0] * (V+1)
    stack = [0] * (V+1)
    top = -1
    # print(S, end=' ') #
    visited[S] = 1
    while True:
        for i in lst[S]:
            if i == G:
                # print(i)  #
                return 1
            if visited[i] == 0:
                top += 1
                stack[top] = S
                S = i
                # print(S, end=' ') #
                visited[S] = 1
                break
        else:
            if top != -1:
                S = stack[top]
                top -= 1
            else:
                return 0

T = int(input())
for idx in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        lst[a].append(b)

    S, G = map(int, input().split())

    # print(lst)
    # print(f'S={S-1}, G={G-1}')
    print(f'#{idx} {dfs(S, G, lst)}')
    # print()
