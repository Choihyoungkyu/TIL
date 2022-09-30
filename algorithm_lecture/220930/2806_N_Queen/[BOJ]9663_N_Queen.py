def f(i, s):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if bit[j] == 0:
            bit[j] = 1
            flag = False
            for k in range(len(s)):
                if abs(k - i) == abs(int(s[k]) - j):
                    flag = True
                    break
            if not flag:
                f(i+1, s+[j])
            bit[j] = 0

N = int(input())
arr = []
bit = [0] * N
cnt = 0
f(0, [])
print(cnt)