import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = input()
    lst = [list(input()) for _ in range(100)]
    maxV = 1
    for i in range(100):
        for j in range(100):
            for l in range(100-j+1):                            # j ~ 100 회문 크기 찾기
                a = []                                          # 찾은 회문을 받을 리스트
                for k in range(l//2):
                    if lst[i][j + k] == lst[i][j + l - 1 - k]:  # 가로 회문 찾기
                        pass
                    else:
                        break
                else:
                    a = lst[i][j:j + l]                         # 찾은 회문 저장
                    if maxV < len(a):                           # 길이가 최대인 회문 찾기
                        maxV = len(a)                           # 회문 길이의 최대값 갱신
                        # res = a                               # 회문 저장

                a = []
                for k in range(l // 2):                         # 세로 회문 찾기
                    if lst[j + k][i] == lst[j + l - 1 - k][i]:
                        pass
                    else:
                        break
                else:
                    for m in range(l):                          # 찾은 회문 저장
                        a.append(lst[j + m][i])
                    if maxV < len(a):                           # 길이가 최대인 회문 찾기
                        maxV = len(a)                           # 회문 길이의 최대값 갱신
                        # res = a                               # 회문 저장


    # print(f'#{idx} {maxV} {res}')
    print(f'#{idx} {maxV}')
