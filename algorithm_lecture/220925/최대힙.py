# 최대힙

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = 2 * p
        else:
            break
    return tmp

heap = [0] * 100
last = 0
for i in range(1, 11):
    enq(i)
for i in range(1, last+1):
    print(heap[i], end=' ')
print()
while last:
    print(deq())