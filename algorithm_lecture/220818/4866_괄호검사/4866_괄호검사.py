# 0.16256s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    s = input()
    cnt1 = 0                    # {} 확인
    cnt2 = 0                    # () 확인
    lst = []                    # 괄호만 받을 리스트 생성

    for i in s:
        if i == '{':            # 중괄호면 리스트에 추가
            lst.append(i)
        elif i == '}':
            lst.append(i)
        elif i == '(':            # 소괄호면 리스트에 추가
            lst.append(i)
        elif i == ')':
            lst.append(i)

    for i in range(len(lst)):
        if lst[i] == '{':         # 대괄호 짝 찾기
            if i+1 < len(lst) and lst[i+1] == ')':  # {)} 인 경우 break
                res = 0
                print(f'#{idx} {res}')
                break
            else:
                cnt1 += 1

        elif lst[i] == '}':
            if 0 <= i-1 and lst[i-1] == '(':  # {(} 인 경우 break
                res = 0
                print(f'#{idx} {res}')
                break
            cnt1 -= 1

        elif lst[i] == '(':       # 소괄호 짝 찾기
            if i+1 < len(lst) and lst[i+1] == '}':  # (}) 인 경우 break
                res = 0
                print(f'#{idx} {res}')
                break
            else:
                cnt2 += 1

        elif lst[i] == ')':
            if 0 <= i-1 and lst[i-1] == '{':  # ({) 인 경우 break
                res = 0
                print(f'#{idx} {res}')
                break
            cnt2 -= 1

    else:
        if cnt1 == 0 and cnt2 == 0:     # 다 돌고나서 각 개수가 0이면 짝이 맞음
            res = 1
        else:                           # 0이 아니면 짝이 안맞음
            res = 0
        print(f'#{idx} {res}')