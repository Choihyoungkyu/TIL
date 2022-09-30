import sys
sys.stdin = open('input.txt')

def f(i, s):
    if i == N:
        tmp = []
        for i in s:
            tmp.append(int(i))
        arr.append(tmp[:])
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
                f(i+1, s+str(j))
            bit[j] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    bit = [0] * N
    f(0, '')
    print(f'#{tc} {len(arr)}')