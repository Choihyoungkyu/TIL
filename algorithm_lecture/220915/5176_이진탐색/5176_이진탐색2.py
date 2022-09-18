import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    DP = [2**i for i in range(11)]
    k = 1
    for i in range(1, 11):
        if N >= DP[i]:
            k = i
        else:
            break
    heap[1] = N // 2 + 1
    tmp = 1
    flag = False
    for i in range(1, k+1):
        for j in range(2**i):
            if tmp == N:
                flag = True
                break
            tmp += 1
            R = 2**(k-i)
            if tmp % 2 == 0:
                heap[tmp] = heap[tmp//2] - R
            else:
                heap[tmp] = heap[tmp//2] + R
        if flag:
            break
    print(k)
    print(heap)
    print(heap[1], heap[N//2])