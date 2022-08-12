import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(arr[i+k][j:j+M])
            # print(tmp)
            tot = 0
            for a in tmp:
                tot += sum(a)
            if tot > maxV:
                maxV = tot
                result = tmp

    print()
    print(f'#{idx} {maxV}')
    for i in result:
        print(*i)
    print()