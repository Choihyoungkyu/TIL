# 0.13473s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input()) // 10
    DP = [[] for _ in range(N+1)]
    DP[0] = 0
    DP[1] = 1
    DP[2] = 3
    for i in range(3, N+1):
        DP[i] = DP[i-2]*2 + DP[i-1]
    print(f'#{idx} {DP[N]}')
