import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    i = int(N**(1/3))
    flag = False
    while i <= int(N**(1/3))+1:
        if i ** 3 == N:
            print(f'#{idx} {i}')
            flag = True
            break
        i += 1
    if not flag:
        print(f'#{idx} -1')
