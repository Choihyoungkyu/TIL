# 실행 시간 : 0.13654s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    a = input()

    num_lst = [0 for _ in range(10)]  # 0~9까지 리스트 생성
    # 문자열로 받은 a를 한개씩 정수로 변환해 그에 해당하는 num_lst 인덱스에 1을 추가
    for i in a:
        num_lst[int(i)] += 1
    maxV = 0  # 개수가 가장 많은 숫자를 담을 변수 생성
    cnt = 0  # 개수가 가장 큰 값을 담을 변수 생성

    # 개수가 가장 많은 숫자와 그 개수를 계산
    for i in range(len(num_lst)):
        if num_lst[i] >= cnt:
            maxV = i
            cnt = num_lst[i]

    print(f'#{idx} {maxV} {cnt}')