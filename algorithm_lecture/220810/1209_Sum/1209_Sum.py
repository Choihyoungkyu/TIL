import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 입력 받은 값들로 100x100 행렬 생성
    max_x = max_y = max_a = max_b = 0

    for i in range(100):
        hap_x = 0  # 각 행의 합 변수
        hap_y = 0  # 각 열의 합 변수
        max_a += arr[i][i]  # 대각선 합
        max_b += arr[i][100 - 1 - i]  # 반대 대각선 합
        for j in range(100):
            hap_x += arr[i][j]  # 각 행의 합
            hap_y += arr[j][i]  # 각 열의 합
        if hap_x >= max_x:  # 행의 최대값 갱신
            max_x = hap_x
        if hap_y >= max_y:  # 열의 최대값 갱신
            max_y = hap_y

    print(f'#{idx} {max(max_x, max_y, max_a, max_b)}')  # 행, 열, 대각선들의 합 중 최대값 출력

