# 방법 1
def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:    # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False                # 검색 실패

# 방법 2 : 재귀 함수 이용
def binarySearch2(a, low, high, key):
    if low > high:              # 검색 실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:    # 검색 성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle-1, high, key)
