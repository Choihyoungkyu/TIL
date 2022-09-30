def f(i, s):
    if i == N:
        tmp = []
        for j in s:
            tmp.append(int(j))
        if tmp not in arr:
            arr.append(tmp[:])
        return
    for j in range(N):
        if bit[j] == 0:
            bit[j] = 1
            f(i+1, s+[j])
            bit[j] = 0
            f(i+1, s+[j])           # 중복을 허용한 전체 부분집합
            f(i+1, s)               # 순서를 고려한 부분집합
N = 3
bit = [0] * N
arr = []
f(0, [])
arr.sort()
for i in arr:
    print(i)
