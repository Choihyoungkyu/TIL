import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]                     # 입력받은 배열
    ni = 0                                                                          # 첫 행
    key = -1                                                                        # brakpoint
    for j in range(100):                                                            # 첫 열부터 시작
        pos = [[0] * 100 for _ in range(100)]                                       # 지나온 경로를 나타낼 배열
        if arr[0][j] == 1:                                                          # 첫 행의 값 중 1인 경우만 탐색
            nj = j                                                                  # nj에 j를 입력
            ni = 0                                                                  # ni에 첫 행을 입력
            while ni < 99:                                                          # 사다리를 다 내려가보자
                pos[ni][nj] = 1                                                     # 첫 시작위치 체크
                if 1 <= nj < 100 and arr[ni][nj-1] == 1 and pos[ni][nj-1] == 0:     # 왼쪽에 사다리가 있고 지나온 경로가 아닐 때
                    nj -= 1                                                         # 왼쪽으로 이동
                    pos[ni][nj] = 1                                                 # 지나온 경로 체크
                elif 0 <= nj < 99 and arr[ni][nj+1] == 1 and pos[ni][nj+1] == 0:    # 오른쪽에 사다리가 있고 지나온 경로가 아닐 때
                    nj += 1                                                         # 오른쪽으로 이동
                    pos[ni][nj] = 1                                                 # 지나온 경로 체크
                else:                                                               # 양쪽에 사다리가 없을 때
                    ni += 1                                                         # 밑으로 이동
                    pos[ni][nj] = 1                                                 # 지나온 경로 체크

                if arr[ni][nj] == 2:                                                # 다 내려왔을 때 값이 2이면
                    pos[ni][nj] = 2                                                 # 지나온 경로 체크
                    print(f'#{idx} {j}')                                            # 출력
                    for s in pos:                                                   # 지나온 경로 출력
                        print(*s)
                    print()
                    key = j                                                         # breakpoint 입력
                    break
        if key >= 0:                                                                # 처음 for문 break
            break



