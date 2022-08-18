import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    dic = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0}      # 개수를 받을 딕셔너리 생성
    for i in dic.keys():                            # 딕셔너리의 key들로 순회
        while True:
            if N % i == 0:                          # i가 N의 약수이면
                dic[i] += 1                         # i의 개수(지수) 증가
                N //= i                             # N 갱신
            else:                                   # 약수를 다 찾으면
                break                               # break
    print(f'#{idx}', end=' ')
    print(*dic.values())