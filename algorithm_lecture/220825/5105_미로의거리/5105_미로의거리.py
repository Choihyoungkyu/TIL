# 0.13437s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):                                              # 시작위치, 도착위치 찾기
        for j in range(N):
            if arr[i][j] == 2:
                s = [i, j]
            elif arr[i][j] == 3:
                e = [i, j]

    def BFS(arr, s, e):
        visited = [[0] * N for _ in range(N)]
        queue = []
        queue.append(s)                                             # 시작위치를 queue에 넣기
        visited[s[0]][s[1]] = 0
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]                      # 하상우좌
        while queue:
            ni, nj = queue.pop(0)                                   # 시작위치부터 탐색 시작
            if ni == e[0] and nj == e[1]:                           # 함수 종료 조건 : 도착 위치에 도달
                return visited[ni][nj] - 1                          # 도착 위치 전까지의 이동 횟수를 구하는 것이므로
            for di, dj in D:
                # 이동 가능한 부분 중 방문 안한 곳
                if 0<=ni+di<N and 0<=nj+dj<N and arr[ni+di][nj+dj]!=1 and visited[ni+di][nj+dj]==0:
                    queue.append([ni+di, nj+dj])                    # 이동 가능하다면 queue에 넣기
                    visited[ni+di][nj+dj] = visited[ni][nj]+1       # 이동 횟수 카운트

    # 출력
    print(f'#{idx}', end=' ')
    if BFS(arr, s, e):
        print(BFS(arr, s, e))
    else:
        print(0)
