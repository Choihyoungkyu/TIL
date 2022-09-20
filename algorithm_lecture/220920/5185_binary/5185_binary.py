import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, s = input().split()
    s = bin(int(s, 16)).lstrip('0b') if s != '0' else '0'   # 16진수 -> 10진수 -> 2진수 변환
    s = '0' * (4*int(N)-(len(s))) + s                       # 앞에 0 붙여주기
    print(f'#{idx} {s}')