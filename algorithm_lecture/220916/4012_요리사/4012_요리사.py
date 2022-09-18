# 부분집합 다 구해서 품
import sys
sys.stdin = open('input.txt')

def f(i):
    if bit.count(1) == N//2:
        tmp = []
        for j in range(N):
            if bit[j] == 1:
                tmp.append(j)
        arr_tmp = tmp[:]
        arr.append(arr_tmp)
    else:
        if i+1 <= N:
            bit[i] = 1
            f(i+1)
            bit[i] = 0
            f(i+1)

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    nums = list(range(N))
    bit = [0] * N
    f(0)
    minV = 40000
    for ar in arr:
        num1 = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                num1 += lst[ar[i]][ar[j]] + lst[ar[j]][ar[i]]

        arr_tmp = []
        for i in range(N):
            if i not in ar:
                arr_tmp.append(i)
        num2 = 0
        for n in range(N // 2):
            for m in range(n + 1, N // 2):
                num2 += lst[arr_tmp[n]][arr_tmp[m]] + lst[arr_tmp[m]][arr_tmp[n]]
        if minV > abs(num1-num2):
            minV = abs(num1-num2)
    print(f'#{idx} {minV}')