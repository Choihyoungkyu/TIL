import sys
sys.stdin = open('input.txt')
from collections import deque

# 운영 비용 = K * K + (K - 1) * (K - 1)
# 수익 : 3 * 집의 수
# 이익 : 수익 - 운영 비용

D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for idx in range(1, int(input())+1):
    N, M = map(int, input().split())        # M : 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        maxV += arr[i].count(1)
    cnt = 1
    flag = False
    for i in range(N):
        for j in range(N):
            cnt_tmp = 0
            q = deque()
            q.append([i, j])
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1
            w = 1
            K = w*w + (w-1)*(w-1)
            if arr[i][j]:
                cnt_tmp += 1
            q_tmp = deque()
            while q and w <= N+1:
                ni, nj = q.popleft()
                for di, dj in D:
                    if 0<=ni+di<N and 0<=nj+dj<N and visited[ni+di][nj+dj] == 0:
                        if arr[ni+di][nj+dj]:
                            cnt_tmp += 1
                        q_tmp.append([ni+di, nj+dj])
                        visited[ni+di][nj+dj] = 1
                if cnt_tmp == maxV and cnt_tmp * M - K >= 0:
                    cnt = cnt_tmp
                    flag = True
                    break
                if q == deque() and q_tmp != deque():
                    w += 1
                    K = w * w + (w - 1) * (w - 1)
                    if cnt_tmp * M - K >= 0 and cnt < cnt_tmp:
                        cnt = cnt_tmp
                    q = q_tmp
                    q_tmp = deque()
            if flag:
                break
        if flag:
            break
    print(f'#{idx} {cnt}')
