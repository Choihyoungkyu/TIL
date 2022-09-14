import sys
sys.stdin = open('input.txt')

N, T = map(int, input().split())
s = list(map(int, input().split()))
lst = [[] for _ in range(N)]
for i in range(0, len(s)-1, 2):         # 연결관계 리스트 만들기
    lst[s[i]-1].append(s[i+1]-1)
    lst[s[i+1]-1].append(s[i]-1)
print(lst)

def DFS(v, N):
    v = v-1                             # Index 맞추기
    stack = [0] * N                     # visited 생성
    visited = [0] * N                   # stack 생성
    top = -1
    print(v+1, end=' ')                 # 문제와 숫자를 맞추기 위해 v+1을 하여 방문 위치 출력
    visited[v] = 1                      # 시작점 방문 표시
    while True:
        for w in lst[v]:
            if visited[w] == 0:         # if ( v의 인접 정점 중 방문 안한 정점 w가 있으면)
                top += 1
                stack[top] = v          # pust(v)
                v = w                   # v <- w (w에 방문)
                print(v+1, end=' ')     # 문제와 숫자를 맞추기 위해 v+1을 하여 방문 위치 출력
                visited[v] = 1          # visited[w] <- True
                break
        else:                           # w가 없다면(갈 수 있는 곳이 없다면)
            if top != -1:               # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                       # 스택이 비어있다면(처음 위치에서 갈 곳이 없다면)
                break                   # while 빠져나오기

DFS(1, N)