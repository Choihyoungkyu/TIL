# 조합
def comb(n, m, j):
    if n == m:
        # arr.append(chosen[:])
        print(chosen)
        return
    else:
        for i in range(j, len(lst)):
            chosen[n] = lst[i]
            comb(n+1, m, i+1)

# 순열
def perm(n, m):
    if n == m:
        # arr.append(chosen[:])
        print(chosen)
        return
    else:
        for i in range(len(lst)):
            chosen[n] = lst[i]
            perm(n+1, m)

N = 4
M = 2
lst = list(range(1, N+1))
arr = []
chosen = [0] * M
# comb(0, M, 0)
perm(0, M)
# for i in arr:
#     print(*i)
# print()