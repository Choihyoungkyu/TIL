import sys
sys.stdin = open('input.txt')

D = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

def DFS(i, j, d, s):
    global maxV
    lst = list(map(int, s.split()))
    if d == 3 and i+D[d][0] == s_i and j+D[d][1] == s_j:
        maxV = max(maxV, len(lst))
        return
    if 0 <= i + D[d][0] < N and 0 <= j + D[d][1] < N and arr[i+D[d][0]][j+D[d][1]] not in lst:
        DFS(i+D[d][0], j+D[d][1], d, s+str(arr[i+D[d][0]][j+D[d][1]])+' ')
        if d != 3:
            DFS(i+D[d][0], j+D[d][1], d+1, s+str(arr[i+D[d][0]][j+D[d][1]])+' ')

for idx in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    for i in range(N):
        for j in range(N):
            s_i, s_j = i, j
            DFS(i, j, 0, str(arr[i][j])+' ')
    print(f'#{idx} {maxV}')


