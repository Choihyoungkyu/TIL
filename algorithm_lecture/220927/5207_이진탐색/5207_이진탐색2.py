import sys
sys.stdin = open('input.txt')

for idx in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for n in B:
        flag = 0
        s = 0
        e = N-1
        # print(n)
        while s <= e:
            m = (s+e) // 2
            # print(s, e, m)
            if n == A[m]:
                cnt += 1
                # print(cnt)
                break
            if n < A[m] and flag != -1:
                flag = -1
                e = m - 1
            elif n > A[m] and flag != 1:
                flag = 1
                s = m + 1
            else:
                break
        # print()
    print(f'#{idx} {cnt}')