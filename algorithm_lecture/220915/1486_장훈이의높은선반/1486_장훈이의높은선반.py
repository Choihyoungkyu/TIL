import sys
sys.stdin = open('input.txt')

# 부분집합을 만들어가며 비교
def f(i, k):
    global maxV
    # 선반의 높이가 됐을 때
    if k == B:
        maxV = k
    # 선반의 높이보다 클 때
    elif k > B:
        if maxV > k:
            maxV = k
    # 부분집합 만들기 -> bit[i] = 1 이면 총합에서 그 숫자를 뺌
    if i < N and k - lst[i] >= B:   # 값을 뺀 총합이 선반보다 클때만 숫자를 뺌
        bit[i] = 1
        f(i + 1, k - lst[i])
        bit[i] = 0
        f(i + 1, k)

T = int(input())
for idx in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    tot = sum(lst)
    bit = [0] * N
    maxV = 99999
    f(0, tot)
    print(f'#{idx} {maxV-B}')