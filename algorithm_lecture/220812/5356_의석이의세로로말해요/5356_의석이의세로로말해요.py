import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    lst = [input() for _ in range(5)]
    lst_2 = []                          # 받아오는 리스트의 각 요소의 길이를 받을 리스트
    for i in range(5):
        s = lst[i]
        lst_2.append(len(s))
    print(f'#{idx}', end=' ')
    for i in range(max(lst_2)):             # 열 순환
        for j in range(5):                  # 행 순환
            if i <= len(lst[j])-1:          # 특정 행의 길이를 벗어난 인덱스를 가질 경우를 대비
                s = lst[j]
                print(s[i], end='')
            else:
                pass
    print()