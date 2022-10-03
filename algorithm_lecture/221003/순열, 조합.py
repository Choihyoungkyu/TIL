
def comb(n, m, j):
    if n == m:
        print(chosen)
        return
    else:
        for i in range(j, len(lst)):
            if lst[i] != 0:
                chosen[n] = lst[i]
                comb(n+1, m, i+1)

def perm(n, m):
    if n == m:
        print(chosen)
    else:
        for i in range(len(lst)):
            if lst[i] != 0:
                chosen[n] = lst[i]
                perm(n+1, m)

N = 4
M = 3
lst = list(range(1, N+1))
arr = []
chosen = [0] * M
# chosen[0] = 3
# lst[2] = 0
# comb(0, M, 0)
# perm(0, M)

