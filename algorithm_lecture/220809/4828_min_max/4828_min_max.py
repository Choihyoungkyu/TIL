#실행 시간 : 0.13239s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    minV = a[0]  # minV와 maxV에 a의 첫번째 값 할당
    maxV = a[0]
    for i in a:  # minV, maxV 값 찾기
        if i < minV:
            minV = i
        elif i > maxV:
            maxV = i
    print(f'#{idx+1} {maxV-minV}')