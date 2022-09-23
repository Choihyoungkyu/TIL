import sys
sys.stdin = open('input.txt')

for idx in range(1, int(input())+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    time.sort(key = lambda x:x[1])
    cnt = 1
    now = time[0][1]
    for i in range(1, N):
        if now <= time[i][0]:
            now = time[i][1]
            cnt += 1
    print(f'#{idx} {cnt}')