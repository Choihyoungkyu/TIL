
import sys
sys.stdin = open('input.txt')

def f(i, N, minV):                                                        # 길이가 N인 부분집합을 생성하는 함수
    if i == N:
        return minV
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N, minV + lst[i][P[i]])
            P[i], P[j] = P[j], P[i]

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]       # 입력 배열
    P = list(range(N))                                              # 한 열당 한 숫자만 오도록 만드는 수열을 만드는데 필요한 리스트
    res = []
    minV = 0
    f(0, N, minV)                                                         # 길이가 N인 부분집합 생성
    print(f'#{idx} {minV}')