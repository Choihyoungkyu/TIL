import sys
sys.stdin = open('input.txt')

def prim(r, V):
    MST = [0] * (V+1)           # MST 포함여부
    MST[r] = 1                  # 시작정점 표시
    s = 0                       # MST 간선의 가중치 합
    for _ in range(V):          # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점 i와 인접한 정점 j 중 MST에 포함되지 않고 가중치가 최소인 정점 u 찾기
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v, E = (map(int, input().split()))
        adjM[u][v] = E
        adjM[v][u] = E
    print(f'#{tc} {prim(0, V)}')
    for i in adjM:
        print(*i)
