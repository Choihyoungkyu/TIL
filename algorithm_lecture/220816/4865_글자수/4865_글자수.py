import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    set1 = set(input())         # 찾을 문자열을 set으로 저장 (중복 X)
    S = input()     
    maxV = 0                    # 최대 개수를 저장할 변수 생성
    for i in set1:              # set1의 각 문자열로 순환
        if maxV < S.count(i):   # 문자의 개수가 최대라면 최대값으로 저장
            maxV = S.count(i)
    print(f'#{idx} {maxV}')