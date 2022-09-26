'''
3
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0
'''

def partition(l, r):
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

for idx in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    qsort(0, N-1)
    print(arr)