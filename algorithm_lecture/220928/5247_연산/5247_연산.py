import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc}', end=' ')
    q = deque()
    q.append(N)
    visited = [1000000] * 1000001
    cnt = 0
    visited[N] = cnt
    tmp = deque()
    while q:
        n = q.popleft()
        if n == M:
            print(cnt)
            break
        if 0 < n+1 <= 1000000 and visited[n+1] > cnt:
            visited[n+1] = cnt
            tmp.append(n + 1)
        if 0 < n-1 <= 1000000 and visited[n-1] > cnt:
            visited[n - 1] = cnt
            tmp.append(n - 1)
        if 0 < 2*n <= 1000000 and visited[2*n] > cnt:
            visited[2*n] = cnt
            tmp.append(2 * n)
        if 0 < n-10 <= 1000000 and visited[n-10] > cnt:
            visited[n - 10] = cnt
            tmp.append(n - 10)
        if q == deque() and tmp != deque():
            q = tmp
            cnt += 1
            tmp = deque()
