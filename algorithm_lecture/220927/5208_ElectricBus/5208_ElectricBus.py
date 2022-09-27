import sys
sys.stdin = open('input.txt')


for idx in range(1, int(input())+1):
    char = list(map(int, input().split()))
    DP = [-1] * (char[0])
    cnt = -1
    for i in range(char[0]-1):
        flag = False
        for j in range(1, char[i+1]+1):
            if i+j < char[0] and DP[i+j] == -1:
                DP[i+j] = DP[i] + 1
    print(DP)
    print(f'#{idx} {DP[-1]}')