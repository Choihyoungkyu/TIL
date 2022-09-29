# Prim / 실패
import sys
sys.stdin = open('input.txt')

def prim(r, V):
    MST = [0] * (V+1)       # MST 포함여부
    MST[r] = 1              # 시작 정점 표시
    s = [0] * (V+1)         # MST 간선의 가중치 합
    for _ in range(V):      # V+1개의 정점 중 v개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        v = 0
        minV = 100
        for i in range(V+1):    # MST에 포함된 정점 i와 인접한 정점 j 중 MST에 포함되지 않고 가중치가 최소인 정점 u 찾기
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        v = i
                        minV = adjM[i][j]
        if s[u] == 0 or s[u] >= s[v] + minV:
            s[u] = s[v] + minV
        MST[u] = 1
    return s

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
    # print(f'#{tc} {prim(0, N)}')
    print(f'#{tc} {prim(0, N)[-1]}')