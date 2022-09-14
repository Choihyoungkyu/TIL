# 시간 복잡도 : O(n)

def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1




a = [2, 5, 6, 13, 19, 4, 5, 1, 18]
a.sort()  # 정렬 후 19의 인덱스는 8
n = len(a)
key = 19
print(sequentialSearch2(a, n, key))