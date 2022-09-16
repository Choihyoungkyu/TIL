import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    p = N
    c = p // 2
    while p > 0:
        if p % 2 == 1:
            tree[c] = tree[p] + tree[p-1]
        else:
            if p+1 > N:
                tree[c] = tree[p]
            else:
                tree[c] = tree[p] + tree[p+1]
        if c == L:
            print(f'#{idx} {tree[c]}')
            break
        p -= 2
        c = p // 2
# 1    2    3    4    5    6    7    8    9    10
# 0    845  671  510  335  501  170  42   468  335