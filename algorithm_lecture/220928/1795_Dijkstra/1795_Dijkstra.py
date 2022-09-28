import sys
sys.stdin = open('input.txt')

# d1 : X에서 나가는 비용
# d2 : X로 들어오는 비용 --> 망함 ㅠㅠ
def dijkstra(N, X, adj1, adj2, d1, d2):
    for i in range(N+1):
        d1[i] = adj1[X][i]
        d2[i] = adj2[i][X]
    U1 = [X]
    U2 = [X]
    for _ in range(N-1):        # N개의 정점 중 시작정점을 제외한 정점 선택
        w1 = 0
        w2 = 0
        for i in range(1, N+1):
            if i not in U1 and d1[i] < d1[w1]:  # 남은 노드 중 비용이 최소인 w
                w1 = i
            if i not in U2 and d2[i] < d2[w2]:  # 남은 노드 중 비용이 최소인 w
                w2 = i
        U1.append(w1)
        U2.append(w2)
        for v in range(1, N+1):                 # 정점 i가
            if 0 <= adj1[w1][v] < 1000000:       # w에 인접이면
                d1[v] = min(d1[v], d1[w1] + adj1[w1][v])
            if 0 <= adj2[w2][v] < 1000000:       # w에 인접이면
                d2[v] = min(d2[v], d2[w2] + adj2[w2][v])



for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    adj1 = [[1000000]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adj1[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
    adj2 = adj1[:]
    Dout = [0] * (N+1)
    Din = [0] * (N+1)
    dijkstra(N, X, adj1, adj2, Dout, Din)
    maxV = 0
    for i in range(1, N+1):
        if i == X:
            continue
        tmp = Dout[i] + Din[i]
        maxV = max(maxV, tmp)
    print(f'#{tc} {Dout} {Din}')
    print(f'#{tc} {maxV}')
    print()