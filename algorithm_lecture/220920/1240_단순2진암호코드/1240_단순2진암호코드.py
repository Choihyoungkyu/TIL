import sys
sys.stdin = open('input.txt')

# 암호코드 : ( (홀수 자리의 합 * 3) + (짝수 자리의 합) ) % 10 == 0
P = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for i in range(N)]
    nums = []
    flag = False

    # 암호코드 정보 찾기
    for n in range(N):
        if '1' in lst[n]:
            for m in range(M-1, -1, -1):
                if lst[n][m] == '1':
                    lst = lst[n][m-55:m+1]
                    flag = True
                    break
        if flag:
            break

    # 암호코드 해독 - 각각의 숫자 찾기
    for i in range(0, 56, 7):
        arr = lst[i:i+7]
        check = []                          # 숫자를 찾기 위한 배열을 담을 리스트
        cnt = 1                             # 배열의 요소(연속된 수)
        for j in range(1, 7):
            if arr[j] == arr[j-1]:
                cnt += 1
                if j == 6:
                    check.append(cnt)
            else:
                check.append(cnt)
                cnt = 1
                if j == 6:
                    check.append(cnt)
        # 찾은 배열로 숫자 찾기
        for k in range(10):
            if check == P[k]:
                nums.append(k)
                break

    # 암호 해독
    tot = (nums[0] + nums[2] + nums[4] + nums[6]) * 3 + nums[1] + nums[3] + nums[5] + nums[7]
    if tot % 10 == 0:
        print(f'#{idx} {sum(nums)}')
    else:
        print(f'#{idx} 0')