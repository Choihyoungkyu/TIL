import sys
from collections import deque
sys.stdin = open('input.txt')

for idx in range(1, 11):
    a, b = map(int, input().split())
    dic = {i:[] for i in range(1, 101)}     # 간선 딕셔너리
    lst = list(map(int, input().split()))   # 배열 입력 받기
    for i in range(0, a, 2):                # 간선 만들기
        if lst[i+1] not in dic[lst[i]]:
            dic[lst[i]].append(lst[i+1])
    visited = [0] * 101                     # 방문 리스트
    queue = deque()
    queue.append(b)                         # 초기 위치를 queue에 입력
    visited[b] = 1                          # 초기 위치를 방문 체크
    tmp = deque()                           # 동시에 이동하기 위한 데크
    maxV = 0                                # 최댓값을 찾기 위한 변수

    # BFS
    while queue:
        t = queue.popleft()
        if maxV < t:                        # 최댓값 찾기
            maxV = t
        for i in dic[t]:                    # 이동 가능한 곳 찾기
            if visited[i] == 0:
                tmp.append(i)
                visited[i] = 1
        if queue == deque() and tmp != deque(): # 한 큐를 다 돌았으면 다음 큐 세팅
            queue = tmp
            tmp = deque()                       # 임시 큐 초기화
            maxV = 0                            # 다음 큐에서 다시 최댓값을 찾기 위해 초기화
    print(f'#{idx} {maxV}')
