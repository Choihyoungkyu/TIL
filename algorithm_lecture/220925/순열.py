def f(i, k, s):
    if i == k:
        print(s)
    elif i != k:
        for j in range(1, k+1):
            if used[j-1] == 0:
                used[j-1] = 1
                f(i+1, k, s+[j])
                used[j-1] = 0

N = 4
used = [0] * N
# used[0] = 1
f(0, N, [])