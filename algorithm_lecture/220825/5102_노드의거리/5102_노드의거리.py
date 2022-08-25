# 0.13368s
import sys
sys.stdin = open('input.txt')

def BFS(dic, S, G):
    visited = [0] * (V+1)
    queue = []
    queue.append(S)                             # 처음 위치를 queue에 넣음
    visited[S] = 0
    while queue:                                # queue에 요소가 있다면
        t = queue.pop(0)                        # 처음 위치부터 시작
        for i in dic[t]:                        # t와 연결된 점들을 순회
            if visited[i] == 0:                 # 방문하지 않았으면
                queue.append(i)                 # queue에 추가
                visited[i] = visited[t] + 1     # visited에 처음 위치로부터 움직인 횟수 입력
                if i == G:                      # 도착 위치에 도달하면 break
                    break
    print(f'#{idx} {visited[G]}')

T = int(input())
for idx in range(1, T+1):
    V, E = map(int, input().split())

    # 경로 생성
    dic = {}
    for i in range(1, V+1):
        dic[i] = []
    for _ in range(E):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    # 시작 위치, 도착 위치
    S, G = map(int, input().split())

    BFS(dic, S, G)

