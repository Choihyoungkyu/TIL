import sys
sys.stdin = open('input.txt')

for idx in range(1, int(input())+1):
    price = list(map(int, input().split()))
    do = list(map(int, input().split()))
    DP = [0] * 12
    DP[0] = min(do[0] * price[0], price[1])
    DP[1] = DP[0] + min(do[1] * price[0], price[1])
    for i in range(2, 12):
        DP[i] = min(DP[i-1] + do[i] * price[0], DP[i-1] + price[1], DP[i-3] + price[2])
    # print(DP)
    print(f'#{idx} {min(DP[-1], price[3])}')