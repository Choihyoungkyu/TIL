# Kruskal / 2352ms
import sys
sys.stdin = open('input.txt')

def leng(x1, x2, y1, y2):
    return (x2-x1)**2 + (y2-y1)**2

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    edge = []
    for i in range(N-1):
        for j in range(i+1, N):
            edge.append([i, j, E * leng(X[i], X[j], Y[i], Y[j])])
    edge.sort(key=lambda x:x[2])
    rep = [i for i in range(N)]
    cnt = 0
    total = 0
    for u, v, w in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == N-1:
                break
    print(f'#{tc} {int(round(total, 0))}')