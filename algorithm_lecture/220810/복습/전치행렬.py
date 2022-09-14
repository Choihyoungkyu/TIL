# 전치행렬 (행과 열을 바꿈)
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] # 4x4 행렬

for k in arr:
    print(*k)
print()

for i in range(4):
    for j in range(4):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
for k in arr:
    print(*k)