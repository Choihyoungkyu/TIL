import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    # 정렬 시작
    for i in range(N-1):                            # 초기 위치
        for j in range(i, N):                       # 비교 위치
            if i % 2 == 0 and a[i] < a[j]:          # 초기 위치가 짝수라면 큰 값이 순서대로 나와야됨
                a[i], a[j] = a[j], a[i]
            elif i % 2 == 1 and a[i] > a[j]:        # 초기 위치가 홀수라면 작은 값이 순서대로 나와야됨
                a[i], a[j] = a[j], a[i]
    print(f'#{idx}', end=' ')                       # 출력
    for i in range(0,10):                           # 값을 10개까지만
        print(a[i], end=' ')
    print()