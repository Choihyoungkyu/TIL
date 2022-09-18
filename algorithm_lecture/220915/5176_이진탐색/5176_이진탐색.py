import sys
sys.stdin = open('input.txt')

def inorder(n):
    global num
    if n:
        if 2*n <= N:
            inorder(2*n)
        heap[n] = num
        num += 1
        if 2*n+1 <= N:
            inorder(2*n+1)

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    num = 1
    inorder(1)
    print(f'#{idx} {heap[1]} {heap[N//2]}')