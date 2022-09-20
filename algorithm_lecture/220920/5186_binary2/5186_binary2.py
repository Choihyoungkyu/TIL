import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = float(input())
    res = ''
    for i in range(1, 13):
        if N >= 2**(-i):
            N -= 2**(-i)
            res += '1'
            if N == 0:
                print(f'#{idx} {res}')
                break
        else:
            res += '0'
    else:
        print(f'#{idx} overflow')