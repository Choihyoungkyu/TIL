# 부분집합_비트연산자
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # n : 원소의 개수
arr.sort()
lst = []
for i in range(1<<n):           # 1<<n : 부분집합의 개수
    tmp = []
    for j in range(n):          # 원소의 수만큼 비트를 비교함
        if i & (1<<j):          # i의 j번 비트가 1인 경우
            tmp.append(arr[j])
             # j번 원소 출력
    lst.append(tmp)
for i in lst:
    print(i)
