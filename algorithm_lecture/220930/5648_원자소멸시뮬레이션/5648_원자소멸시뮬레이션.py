import sys
sys.stdin = open('input.txt')

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 하상좌우

for tc in range(1, int(input())+1):
    N = int(input())
    x_lst = []
    y_lst = []
    x, y, d, K = map(int, input().split())
