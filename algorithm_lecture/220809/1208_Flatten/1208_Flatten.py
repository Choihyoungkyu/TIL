import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    D = int(input())
    H = list(map(int, input().split()))

    for _ in range(D):  # 덤프 진행
        H[H.index(max(H))] -= 1  # 최대값을 찾고 1을 뺌
        H[H.index(min(H))] += 1  # 최소값을 찾고 1을 더함

    print(f'#{idx} {max(H) - min(H)}')