# 0.14877s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    price = list(map(int, input().split()))     # 이용권 가격 (1일, 1달, 3달, 1년 이용권)
    mon = list(map(int, input().split()))       # 이용 계획

    mon_price = []
    for i in mon:
        if i * price[0] > price[1]:
            mon_price.append(price[1])
        else:
            mon_price.append(i * price[0])
    DP = [0] * 12
    DP[0] = mon_price[0]
    DP[1] = DP[0] + mon_price[1]
    DP[2] = min(DP[1] + mon_price[2], price[2])
    for i in range(3, 12):
        DP[i] = min(DP[i-1] + mon_price[i], DP[i-3] + price[2])


    print(f'#{idx} {min(DP[11], price[3])}')