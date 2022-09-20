
import sys
sys.stdin = open('input.txt')

# 암호코드 : ((홀수 자리의 합 * 3) + 짝수 자리의 합 + 검증코드) % 10 == 0
P = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2], [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3], [1, 1, 2]]

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(input() for _ in range(N))
    res = 0
    s_check = []
    for i in range(1, N-1):
        s = ''
        if lst[i] == '0'*M:
            continue
        for j in range(1, M-1):
            if lst[i][j] != '0' and lst[i-1][j] == '0' and lst[i][j] == lst[i+1][j]:
                s += lst[i][j]
            elif lst[i][j-1] == '0' and lst[i][j+1] == '0' and s in s_check:
                s = ''
        if s != '':
            s = bin(int(s, 16)).strip('0b')
            if s not in s_check:
                print(s, len(s))
                s_check.append(s)
                j = 1
                cnt = 1
                tmp = 0
                check = []
                final = []
                while j < len(s):
                    if s[j] == s[j-1]:
                        cnt += 1
                        if j == len(s)-1:
                            check.append(cnt)
                            final.append(check[:])
                    else:
                        tmp += 1
                        if tmp == 4:
                            tmp = 0
                            final.append(check[:])
                            check = []
                        else:
                            check.append(cnt)
                        cnt = 1
                        if j == len(s)-1:
                            check.append(cnt)
                            final.append(check[:])
                    j += 1

    print(final)