# 0.15341s
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx, N = map(int, input().split())
    lst = [[] for _ in range(100)]
    s = list(map(int, input().split()))             # 연결관계 입력값
    for i in range(0, 2*N, 2):
        lst[s[i]].append(s[i+1])                    # 연결관계 리스트
    v = 0                                           # 탐색 시작 위치
    w = 99                                          # 탐색 종료 위치
    def dfs(v, w, lst):
        visited = [0] * 100                         # 방문한 곳 표시할 리스트
        stack = [0] * 100                           # 되돌아 갈 곳 리스트
        top = -1
        visited[v] = 1                              # 시작 위치
        while True:
            for i in lst[v]:                        # 현재 위치에서 연결된 곳으로 이동
                if i == w:                          # 이동할 곳이 목표 위치면
                    return 1                        # 탐색 종료
                if visited[i] == 0:                 # 이동할 곳이 처음 방문이라면
                    top += 1
                    stack[top] = v                  # 현재 위치를 스택에 저장
                    visited[i] = 1                  # 방문한 곳 표시
                    v = i                           # 현재 위치를 이동
                    break

            else:                                   # 현재 위치에서 갈 곳이 없다면
                if top != -1:                       # 빈 스택이 아니라면
                    v = stack[top]                  # 이전 위치로 이동
                    top -= 1
                else:                               # 빈 스택이라면
                    return 0                        # 탐색 실패
    print(f'#{idx} {dfs(v, w, lst)}')