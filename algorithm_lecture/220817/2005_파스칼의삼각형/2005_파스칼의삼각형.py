# 0.13256s
import sys
sys.stdin = open('input.txt')

DP = [[] for _ in range(10)]                # DP 리스트 만들기
DP[0] = [1]                                 # 초기값 설정
DP[1] = [1, 1]
for i in range(3, 11):                      # 인덱스를 i-1로 잡기 위해서 i는 10까지 해야됨
    for j in range(len(DP[i-2])-1):         # 다음 삼각형 밑변을 만들기 위해 이전 삼각형 밑변 이용
        DP[i-1].append(DP[i-2][j] + DP[i-2][j+1])   # 이전 삼각형의 연속된 두 수의 합을 추가
    DP[i-1] = [1] + DP[i-1] + [1]           # 양 옆에 1을 추가

T = int(input())                            # 테스트케이스 출력
for idx in range(1, T+1):
    N = int(input())
    print(f'#{idx}')
    for i in DP[:N]:                        # 삼각형 출력
        print(*i)