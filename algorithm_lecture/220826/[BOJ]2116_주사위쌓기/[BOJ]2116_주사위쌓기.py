import sys
input = lambda : sys.stdin.readline().strip()

def f(num):
    if num == 0: return 5
    elif num == 1: return 3
    elif num == 2: return 4
    elif num == 3: return 1
    elif num == 4: return 2
    elif num == 5: return 0

# A-F, B-D, C-E
# A, B, C, D, E, F
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(6):
    tmp_max = 0
    idx = 0
    stack = []
    stack.append(lst[idx][f(i)])
    for j in range(6):
        if j == i or j == f(i):
            pass
        else:
            if lst[idx][j] > tmp_max:
                tmp_max = lst[idx][j]
    # print(tmp_max)
    while idx != N-1:
        tmp = 0
        idx += 1
        t = stack.pop(0)
        for j in range(6):
            if lst[idx][j] == t:
                tmp_j = j
        for j in range(6):
            if j == tmp_j or j == f(tmp_j):
                pass
            else:
                if lst[idx][j] > tmp:
                    tmp = lst[idx][j]
        stack.append(lst[idx][f(tmp_j)])
        # print(tmp)
        tmp_max += tmp
    # print(tmp_max)
    if tmp_max >= maxV:
        maxV = tmp_max
    # print()
print(maxV)
