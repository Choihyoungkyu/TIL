arr = [1, 2, 3, 4]
n = len(arr)

lst = []
for i in range(0, 1<<n):    # 1<<n : 부분집합의 개수
    tmp = []
    for j in range(0, n):   # 원소의 수만큼 비트를 비교
        if i & (1<<j):      # i의 j번째 비트가 1이면 j번째 원소 출력
            tmp.append(arr[j])
    lst.append(tmp[:])
for i in lst:
    print(i)
