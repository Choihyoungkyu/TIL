# 실행 시간 : 0.12577s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [0] * 5000  # 5000개의 버스 정류장 리스트 생성
    for i in range(1, N+1):  # 버스가 지나갈때마다 해당 정류장 숫자 1 증가
        A, B = map(int, input().split())
        for j in range(A-1, B):
            lst[j] += 1

    P = int(input())
    C = []  # 출력할 정류장을 받을 빈 리스트 생성
    for _ in range(P):  # 입력 받은 숫자에 해당하는 인덱스의 값을 C에 추가
        c = int(input())
        C.append(lst[c-1])
    text = ''
    for k in range(P):
        text += str(C[k]) + ' '
    print(f'#{idx} {text}')
