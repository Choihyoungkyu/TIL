import sys
sys.stdin = open('input.txt')

def back(i, s):
    for j in range(1, battery[i]+1):
        if i+j <= N-1:
            if check[i+j] >= s+1:
                check[i+j] = s+1
                back(i+j, s+1)


for idx in range(1, int(input())+1):
    N, *battery = map(int, input().split())
    battery += [0]
    check = [100] * N
    check[0] = 0
    back(0, -1)
    print(f'#{idx} {check[-1]}')

'''
[-1, 0, 0, 1, 1]
#1 1
[-1, 0, 0, 1, 1, 1, 2, 2, 2, 2]
#2 2
[-1, 0, 1, 2, 2, 3, 3, 4, 5, 5]
#3 5
'''