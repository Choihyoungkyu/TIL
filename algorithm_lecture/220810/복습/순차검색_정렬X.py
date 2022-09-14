# 시간 복잡도 : O(n)

def sequentialSearch(a, n, key):  # a : 배열, n : n번 안에 찾아라는 의미, key : 목표값
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1  # Search Fail

a = [2, 5, 6, 13, 19, 4, 5, 1, 18]
n = len(a)
key = 19
print(sequentialSearch(a, n, key))