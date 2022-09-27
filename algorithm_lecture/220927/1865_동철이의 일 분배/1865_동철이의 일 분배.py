# 상찬님의 도움을 받아 해결
import sys
sys.stdin = open('input.txt')

def f(i, k, s):
    global maxV
    if i == k and s > maxV:
        maxV = s
    elif s * (max_lst ** (k-1-i)) < maxV:
        return
    else:
        for j in range(N):
            if bit[j] == 0 and lst[i][j]:
                bit[j] = 1
                f(i+1, k, s*lst[i][j])
                bit[j] = 0

for idx in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    max_lst = 0
    for i in range(N):
        max_lst = max(max_lst, max(lst[i]))
    maxV = 0
    bit = [0] * N
    f(0, N, 1)
    print(f'#{idx} {maxV*100:.6f}')