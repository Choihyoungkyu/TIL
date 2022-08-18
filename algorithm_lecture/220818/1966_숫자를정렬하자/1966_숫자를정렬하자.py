# 0.14598s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    i = 0
    while i < len(num)-1:
        if num[i] > num[i+1]:                       # 앞의 수가 뒤의 수보다 크면
            num[i], num[i+1] = num[i+1], num[i]     # 자리 바꾸기
            if i != 0:
                i -= 1                              # 바꾼 수와 이전 수를 비교하기 위해
        else:
            i += 1
    print(f'#{idx}', end=' ')
    print(*num)