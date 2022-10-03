arr = [1, 2, 3, 4]
n = len(arr)

# 비트 연산자를 이용한 부분집합 구하는 방법
lst = []
for i in range(0, 1<<n):    # 1<<n : 부분집합의 개수
    tmp = []
    for j in range(0, n):   # 원소의 수만큼 비트를 비교
        if i & (1<<j):      # i의 j번째 비트가 1이면 j번째 원소 출력
            tmp.append(arr[j])
    lst.append(tmp[:])
for i in lst:
    print(i)

# 재귀를 이용한 부분집합 구하는 방법
# chosen = [0] * n
# lst = []
# def comb(n, m, j, res):
#     if n == m :
#         lst.append(res[:])
#         return
#     else:
#         for i in range(j, len(arr)):
#             chosen[n] = arr[j]
#             comb(n+1, m, i+1, res+[chosen[n]])
#             comb(n+1, m, i+1, res)
#
# comb(0, 4, 0, [])
# for i in lst:
#     print(i)
