import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
M = int(input())
lst = list(map(int, input().split()))
C = 100
K = N-C
# N-C보다 작으면 채널 누르기로 ㄱㄱ
cnt = 0
square = 0
while N != 0:
    tmp = N%10
    if tmp not in lst:
        cnt += 1
    else:
