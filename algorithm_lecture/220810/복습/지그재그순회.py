# 지그재그 순회
N, M = 3, 4
arr = [[8, 5, 6, 1],[1, 5, 3, 2], [7, 0, 1, 9]]

for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i % 2)], end=' ')
    print()

# 지그재그 순회(column)