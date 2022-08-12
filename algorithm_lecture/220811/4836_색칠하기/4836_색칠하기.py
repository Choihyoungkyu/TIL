import sys
sys.stdin = open('input.txt')

# color 1 : 빨강
# color 2 : 파랑

T = int(input())
for idx in range(1, T+1):
    arr = [[0]*11 for _ in range(11)]                   # 0~10 배열 생성
    N = int(input())
    for _ in range(N):                                  # N개의 색종이
        x1, y1, x2, y2, c = map(int, input().split())
        for i in range(x1, x2+1):                       # 색종이 덮기
            for j in range(y1, y2+1):
                arr[i][j] += c                          # 색에 따라 다른 숫자 더하기

    cnt = 0                                             # 보라색의 넓이 구하기
    for i in arr:
        cnt += i.count(3)
        print(*i)
    print(f'#{idx} {cnt}')
    print()