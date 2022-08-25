# 0.15284s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for _ in range(M%N):                        # N만큼 돌면 원래자리
        queue.append(queue.pop(0))
    print(f'#{idx} {queue[0]}')