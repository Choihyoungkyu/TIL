import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

for idx in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    last = 0
    heap = [0] * (N+1)
    for n in lst:
        enq(n)
    res = 0
    while last:
        last //= 2
        res += heap[last]
    print(f'#{idx} {res}')