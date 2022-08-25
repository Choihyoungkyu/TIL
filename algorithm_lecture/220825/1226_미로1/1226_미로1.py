# 0.16106s
import sys
sys.stdin = open('input.txt')

def BFS(lst, S, G):
    D = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 상하우좌
    queue = []
    queue.append(S)                         # queue에 처음 위치 추가
    visited = [[1] * 16 for _ in range(16)] # 방문 체크 리스트 생성 (1이면 방문 안한거)
    visited[S[0]][S[1]] = 0                 # 처음 위치 방문체크
    while queue:                            # queue에 요소가 있다면
        ni, nj = queue.pop(0)               # queue의 첫번째 요소를 팝한 후 현재 위치로 사용
        for di, dj in D:                    # 4방향 탐색
            if 0<=ni+di<16 and 0<=nj+dj<16 and lst[ni+di][nj+dj] != 1 and visited[ni+di][nj+dj] != 0:
            # 현재 위치와 방문을 하지 않은 연결된 경로가 있다면
                queue.append([ni+di, nj+dj])
                visited[ni+di][nj+dj] = 0
                if ni+di == G[0] and nj+dj == G[1]:     # 도착 위치에 도달했다면 1을 리턴
                    return 1
    return 0                                # 다 돌았는데 도착 위치로 못간다면 0을 리턴

for _ in range(10):
    idx = int(input())
    lst = [list(map(int,input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                S = [i, j]
            elif lst[i][j] == 3:
                G = [i, j]
    print(f'#{idx} {BFS(lst, S, G)}')