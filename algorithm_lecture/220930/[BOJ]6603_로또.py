import sys
input = lambda:sys.stdin.readline().strip()

def comb(n, m, j):
    if n == m:
        arr.append(chosen[:])
        return
    else:
        for i in range(j, len(lst)):
            chosen[n] = lst[i]
            comb(n+1, m, i+1)

while True:
    N, *lst = map(int, input().split())
    if N == 0:
        break
    arr = []
    chosen = [0] * (6)
    comb(0, 6, 0)
    for i in arr:
        print(*i)
    print()