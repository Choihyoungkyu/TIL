# 0.18209s
import sys
from collections import deque
sys.stdin = open('input.txt')

# 1 : 사방, 2 : ㅣ, 3 : ㅡ, 4 : ㄴ, 5 : r, 6 : ㄱ, 7 : ┘
T = int(input())
for idx in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    l = 1
    visited = [[0] * M for _ in range(N)]
    tmp_queue = deque()
    queue = deque()
    queue.append([R, C])
    visited[R][C] = 1
    while queue and l < L:
        i, j = queue.popleft()
        # 터널 : 1
        if lst[i][j] == 1:
            tmp = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:   # 하, 상, 우, 좌
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and ni<N and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 4 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and 0<=ni and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 5 or lst[ni][nj] == 6):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 3 and nj<M and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 6 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 4 and 0<=nj and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 4 or lst[ni][nj] == 5):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 : 2
        elif lst[i][j] == 2:
            tmp = 0
            for di, dj in [[1, 0], [-1, 0]]:   # 하, 상
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and ni<N and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 4 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and 0<=ni and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 5 or lst[ni][nj] == 6):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 3
        elif lst[i][j] == 3:
            tmp = 0
            for di, dj in [[0, 1], [0, -1]]:   # 우, 좌
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and nj<M and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 6 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and 0<=nj and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 4 or lst[ni][nj] == 5):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 : 4
        elif lst[i][j] == 4:
            tmp = 0
            for di, dj in [[-1, 0], [0, 1]]:   # 상, 우
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and 0<=ni and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 5 or lst[ni][nj] == 6):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and nj<M and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 6 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 : 5
        elif lst[i][j] == 5:
            tmp = 0
            for di, dj in [[1, 0], [0, 1]]:   # 하, 우
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and ni<N and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 4 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and nj<M and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 6 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 : 6
        elif lst[i][j] == 6:
            tmp = 0
            for di, dj in [[1, 0], [0, -1]]:   # 하, 좌
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and ni<N and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 4 or lst[ni][nj] == 7):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and 0<=nj and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 4 or lst[ni][nj] == 5):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt

        # 터널 : 7
        elif lst[i][j] == 7:
            tmp = 0
            for di, dj in [[-1, 0], [0, -1]]:   # 상, 좌
                tmp += 1
                ni, nj = i+di, j+dj
                if tmp == 1 and 0<=ni and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 2 or lst[ni][nj] == 5 or lst[ni][nj] == 6):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
                if tmp == 2 and 0<=nj and not visited[ni][nj] and (lst[ni][nj] == 1 or lst[ni][nj] == 3 or lst[ni][nj] == 4 or lst[ni][nj] == 5):
                    tmp_queue.append([ni, nj])
                    cnt += 1
                    visited[ni][nj] = cnt
        if queue == deque() and tmp_queue != deque():
            queue = tmp_queue
            l += 1
            tmp_queue = deque()

    # for i in visited:
    #     print(*i)
    print(f'#{idx} {cnt}')