# Prim / 24925ms
import sys
sys.stdin = open('input.txt')

def leng(x1, x2, y1, y2):
    return (x2-x1)**2 + (y2-y1)**2

def prim(r, V):
    MST = [0] * (V)
    MST[r] = 1
    s = 0
    for _ in range(V-1):
        u = r
        minV = 2000000
        for i in range(V):
            if MST[i] == 1:
                for j, w in adjL[i]:
                    if MST[j] == 0 and minV > w:
                        u = j
                        minV = w
        s += minV
        MST[u] = 1
    return s

for tc in range(1, int(input())+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    adjL = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            adjL[i].append([j, E * leng(X[i], X[j], Y[i], Y[j])])
            adjL[j].append([i, E * leng(X[i], X[j], Y[i], Y[j])])
    # for idx, i in enumerate(adjL):
    #     print(idx, i)
    print(f'#{tc} {int(round(prim(0, N), 0))}')