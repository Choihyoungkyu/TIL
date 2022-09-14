N, M = map(int, input().split())
arr = [list(range(M)) for _ in range(N)]

di = [0, 0, -1, 1] # 상하좌우
dj = [-1, 1, 0, 0]

# 방법
for i in range(N):
    for j in range(M):
        for k in range(k):  # 4방향 순회
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:  # 유효한 인덱스면 (=인덱스 에러가 안나면)
                print(arr[ni][nj])  # 해당 칸의 상하좌우에 해당하는 칸을 출력

# 응용 (상하좌우 2칸씩 탐색)
for i in range(N):
	for j in range(M):
        for k in range(4):  # 4방향 순회
            for d in range(1, 3):  # 1칸, 2칸
                ni = i + (di[k] * d)
                nj = j + (dj[k] * d)
                if 0 <= ni < N and 0 <= nj < N  # 유효한 인덱스면 (=인덱스 에러가 안나면)
                    print(arr[ni][nj])