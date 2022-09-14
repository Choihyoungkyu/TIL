# 시간 복잡도 : O(kn)
# k번째로 작은 원소를 찾을 때

def select(a, k):
    for i in range(0, k):               # k번째까지 반복
        minIdx = i
        for j in range(i+1, len(a)):    # 배열 a 전체 탐색
            if a[minIdx] > a[j]
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return a[k-1]