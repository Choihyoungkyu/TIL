import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, -1, 1]  # 상하좌우
    dj = [1, -1, 0, 0]

    tot = 0  # 합을 받을 변수 생성
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]  # 칸의 좌우에 대한 인덱스
                nj = j + dj[k]  # 칸의 상하에 대한 인덱스
                if 0<=ni<N and 0<=nj<N:  # 행렬을 벗어나지 않도록 하는 조건
                    tot += abs(arr[i][j] - arr[ni][nj])  # 칸 - (상, 하, 좌, 우) 의 절대값 더함
    print(tot)