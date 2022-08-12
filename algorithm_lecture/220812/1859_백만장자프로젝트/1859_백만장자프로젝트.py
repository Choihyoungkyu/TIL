import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))  # 매매가
    money = 0
    maxV = max(lst)
    for i in range(N):
        if lst[i] == maxV and i+1<len(lst):
            maxV = max(lst[i+1:])
            continue
        elif lst[i] < maxV:
            money += maxV - lst[i]
    print(f'#{idx} {money}')