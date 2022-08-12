# 실행 시간 : 0.14268s

import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = [0 for i in range(N+1)]  # 충전기 위치를 나타낼 리스트 생성
    c = list(map(int, input().split()))  # 충전기 위치를 받아서 리스트로 나타냄
    for i in c:  # 충전기 위치 입력
        charge[i] = 1

    maxV = 0  # 충전 후 버스가 돌아다닌 거리
    cnt = 0  # 충전 횟수
    for i in range(1, N+1):  # 1~N까지 반복문
        maxV += 1  # 매 반복마다 버스가 움직인 거리

        # 최대 이동 횟수를 넘어서면 즉시 종료
        if maxV > K:
            print(f'#{idx} 0')
            break

        # 마지막 부분 최대 이동 거리에 해당하는 충전소가 있을 경우 즉시 종료
        if i == (N - K) and charge[i] == 1:
            cnt += 1
            print(f'#{idx} {cnt}')
            break

        # 최대 이동거리에 해당하는 정류소가 있으면 충전
        if charge[i] == 1 and maxV == K:
            maxV = 0
            cnt += 1   
        # 최대 이동거리 전에 정류소가 있지만 뒤쪽 정류소가 최대 이동거리를 벗어날 경우 충전
        # 즉, 뒤쪽 정류소가 최대 이동거리 내에 있다면 이번 정류소를 뛰어넘음
        elif (charge[i] == 1) and (1 not in charge[i+1:i+1+K-maxV]):
            maxV = 0
            cnt += 1

    else:
        print(f'#{idx} {cnt}')
