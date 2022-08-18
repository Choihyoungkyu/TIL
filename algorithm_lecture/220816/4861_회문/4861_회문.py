import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]                 # 문자열 리스트 생성
    a = []                                                  # 찾은 회문을 저장할 리스트
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):                           # 가로 회문 찾기
                if lst[i][j + k] == lst[i][j + M - 1 - k]:
                    pass
                else:
                    break
            else:
                a = lst[i][j:j+M]                           # 찾은 회문 저장
                break

            for k in range(M//2):                           # 세로 회문 찾기
                if lst[j + k][i] == lst[j + M - 1 - k][i]:
                    pass
                else:
                    break
            else:
                for m in range(M):                          # 찾은 회문 저장
                    a.append(lst[j+m][i])

    print(f'#{idx}', end=' ')
    print(''.join(a))