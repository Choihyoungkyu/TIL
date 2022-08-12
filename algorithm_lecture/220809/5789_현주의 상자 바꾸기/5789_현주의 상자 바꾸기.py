# 실행 시간 : 537ms
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, Q = map(int, input().split())
    lst = [0] * N  # 상자 리스트 생성
    for i in range(1, Q+1):  # 상자 리스트 갱신
        L, R = map(int, input().split())
        lst[L-1:R] = [i]*(R-L+1)
    text = ''
    for j in lst:
        text += str(j) + ' '
    print(f'#{idx} {text}')