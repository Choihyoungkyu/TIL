import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    A, B = input().split()
    cnt = A.count(B)        # A에 있는 B를 다 셈
    lst = A.split(B)        # B를 기준으로 스플릿
    for i in lst:           # 스플릿 된 각각의 문자열의 길이를 더함 (공백은 0을 더함)
        cnt += len(i)
    print(f'#{idx} {cnt}')
