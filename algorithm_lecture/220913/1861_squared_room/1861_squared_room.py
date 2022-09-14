# 1.22296s
import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    D = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    fre = 0                     # 최대 연속된 수
    minV = N**2                 # 최대 연속된 수를 가진 요소
    # 처음부터 끝까지 다 돌면서 한 케이스씩 다 진행
    for i in range(N):
        for j in range(N):
            cnt = 1             # 매 케이스마다 연속된 수 초기화
            flag = False        # 가지치기용
            queue = deque()
            queue.append([i, j])
            # DFS
            while queue:
                ni, nj = queue.popleft()
                for di, dj in D:
                    # 상하좌우 중 하나가 자신보다 1이 작다면 다음으로 넘어감 -> 가지치기
                    if 0<=ni+di<N and 0<=nj+dj<N and cnt == 1 and lst[ni+di][nj+dj] == lst[ni][nj]-1:
                        flag = True
                        break
                    # 1보다 크면
                    if 0<=ni+di<N and 0<=nj+dj<N and lst[ni+di][nj+dj] == lst[ni][nj]+1:
                        cnt += 1
                        queue.append([ni+di, nj+dj])
                        break
                # 가지치기 됐으면
                if flag:
                    break
            # 연속된 수가 더 많은 경우
            if cnt > fre:
                fre = cnt
                minV = lst[i][j]
            # 연속된 수가 같은 경우
            elif cnt == fre:
                if minV > lst[i][j]:    # 더 작은 숫자를 채택
                    fre = cnt
                    minV = lst[i][j]
    print(f'#{idx} {minV} {fre}')