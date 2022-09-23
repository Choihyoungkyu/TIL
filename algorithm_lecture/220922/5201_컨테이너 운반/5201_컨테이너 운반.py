import sys
sys.stdin = open('input.txt')

for idx in range(1, int(input())+1):
    N, M = map(int, input().split())        # N : 컨테이너 수, M : 트럭 수
    W = list(map(int, input().split()))     # W : 화물의 무게
    T = list(map(int, input().split()))     # T : 트럭의 적재용량
    W.sort(reverse=True)
    T.sort()
    tot = 0
    check = [1] * N
    for t in T:
        for i in range(N):
            if check[i] and W[i] <= t:      # 트럭에 컨테이너 한개 넣으면 끝
                tot += W[i]
                check[i] = 0
                break
    print(f'#{idx} {tot}')