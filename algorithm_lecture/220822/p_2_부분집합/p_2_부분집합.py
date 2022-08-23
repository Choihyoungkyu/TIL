def f(i, k):                            # i : 시작위치, k : 부분집합의 합
    if k == 10:
        for i in range(10):
            if bit[i]:
                print(lst[i], end=' ')
        print()
        return
    elif i == 10:                       # 다 돌았는데 부분집합의 합이 10이 안되면 return
        return
    else:
        if k + lst[i] <= 10:            # 부분집합의 합이 10을 넘어가면 그 이후는 안봄
            bit[i] = 1                      # lst[i]를 부분집합에 포함
            f(i+1, k + lst[i])          # bit[i]가 1인 경우의 k로 재귀
            bit[i] = 0
            f(i+1, k)                   # bit[i]가 0인 경우의 k로 재귀

lst = list(range(1, 11))
bit = [0] * 10
f(0, 0)