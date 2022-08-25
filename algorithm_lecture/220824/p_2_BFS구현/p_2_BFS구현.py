import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
dic = {}
for i in range(1, N+1):                     # 1~N까지의 리스트를 value로 가지는 key를 생성
    dic[i] = []
tmp = list(map(int, input().split()))       # 입력값
for i in range(0, 2*K, 2):                  # 받은 입력값으로 dic에 경로 생성
    dic[tmp[i]].append(tmp[i+1])
    dic[tmp[i+1]].append(tmp[i])

def BFS(G, v, n):                           # G : graph, v : start, n : N
    visited = [0]*(n+1)
    queue = []
    queue.append(v)                         # 시작 위치를 queue에 넣음
    visited[v] = 1                          # 시작 위치를 방문 체크
    while queue:                            # queue에 요소가 있는 동안
        t = queue.pop(0)
        print(-t, end='')                   # 경로 출력
        for i in dic[t]:                    # 이동한 위치에 연결된 경로들
            if visited[i] == 0:             # 연결된 경로 중 방문 안한 곳만
                queue.append(i)             # queue에 넣고
                visited[i] = 1              # 방문 체크
BFS(dic, 1, N)