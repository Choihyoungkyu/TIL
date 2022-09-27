import sys
sys.stdin = open('input.txt')

def bin_search(l, r, n):
    global flag
    global tmp

    m = (l+r)//2

    if n == A[m]:
        tmp = 1
        return tmp

    if l >= r:
        tmp = 0
        return tmp

    if n < A[m] and (flag == 1 or flag == 0):
        r = m - 1
        flag = -1
        bin_search(l, r, n)

    elif n > A[m] and (flag == -1 or flag == 0):
        l = m + 1
        flag = 1
        bin_search(l, r, n)

    else:
        tmp = 0
        return tmp


for idx in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for n in B:
        tmp = 0
        flag = 0
        bin_search(0, len(A)-1, n)
        cnt += tmp

    print(f'#{idx} {cnt}')