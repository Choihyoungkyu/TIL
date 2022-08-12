# 실행 시간 : 0.12735s
import sys
sys.stdin = open('input.txt')

'''
10 3
1 2 3 4 5 6 7 8 9 10
'''

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    minV = maxV = 0
    for i in range(M):  # 초기값 설정
        minV += a[i]  # 첫 배열의 합을 최솟값으로 설정
        maxV += a[i]  # 첫 배열의 합을 최댓값으로 설정

    for i in range(N-M+1):  # 0 ~ N-M 순회
        tot = 0  # 각 케이스별 합을 받을 변수 생성
        for j in range(M):  # 각 케이스별 합을 구한 뒤 조건에 따라 최대, 최소 갱신
            tot += a[i + j]
        if tot > maxV:
            maxV = tot
        if tot < minV:
            minV = tot

    print(f'#{idx} {maxV-minV}')