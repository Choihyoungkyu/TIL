import sys
sys.stdin = open('input.txt')

T = int(input())

A = list(range(1, 13))                          # 1~12 리스트 생성
for idx in range(1, T+1):                       
    N, K = map(int, input().split())            # N : 부분집합의 크기, K : 부분집합의 합
    cnt = 0                                     # cnt : 조건을 만족하는 부분집합의 수
    for i in range(1 << 12):                    # 리스트 A의 부분집합의 수만큼 순회
        tmp = []                                # tmp : 각 부분집합을 나타낼 리스트
        for j in range(12):                     # 리스트 A의 길이만큼 순회
            if i & (1 << j):                    # 비트연산자를 통한 부분집합 탐색
                tmp.append(A[j])                
        if len(tmp) == N and sum(tmp) == K:     # 부분집합의 길이가 N이고 그 합이 K일 경우
            cnt += 1                            # 카운트 1 증가
    print(f'#{idx} {cnt}')