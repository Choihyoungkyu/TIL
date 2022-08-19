#
import sys
sys.stdin = open('input.txt')

def fn(price, mon):
    mon_price = [0] * 12
    for i in range(12):
        if mon[i] * price[0] <= price[1]:
            mon_price[i] = mon[i] * price[0]
        else:
            mon_price[i] = price[1]


    cnt = 0
    print(*price)
    while True:
        Three = []
        for j in range(len(mon_price)-2):
            Three.append(mon_price[j] + mon_price[j + 1] + mon_price[j + 2])
        print(f'mon_price = {mon_price}')
        print(f'Three     = {Three}')
        max_k = 0
        Idx_k = -1
        for k in range(len(mon_price)-2):
            if Three[k] >= price[2]:
                if max_k < Three[k]:
                    max_k = Three[k]
                    Idx_k = k
        if Idx_k >= 0 :
            mon_price.pop(Idx_k)
            mon_price.pop(Idx_k)
            mon_price.pop(Idx_k)
            cnt += 1
        else:
            break

    tot = cnt * price[2]
    for m in mon_price:
        tot += m
    if tot > price[3]:
        return price[3]
    else:
        return tot




T = int(input())
for idx in range(1, T+1):
    price = list(map(int, input().split()))     # 이용권 가격 (1일, 1달, 3달, 1년 이용권)
    mon = list(map(int, input().split()))       # 이용 계획
    print(f'#{idx} {fn(price, mon)}')