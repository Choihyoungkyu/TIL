import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    arr = list(map(int, input().split()))  # 입력 받은 값들로 1차원 리스트 생성
    cnt = 0  # 0과 1을 반환할 변수 생성
    for i in range(1 << 10):  # 2^10, 즉 0 ~ 1023의 순회 실시
        tmp = []  # 각 부분집합을 받을 리스트 생성 및 초기화
        for j in range(10):
            if i & (1 << j):  # 비트연산자를 통해 부분집합 찾기
                tmp.append(arr[j])  # 찾은 요소를 리스트에 저장
        if sum(tmp) == 0 and len(tmp) != 0:  # 찾은 부분집합 요소들의 합이 0이고 공집합이 아니라면
            cnt = 1  # 1을 저장
            break  # 하나만 찾아도 되므로 break
    print(f'#{idx} {cnt}')