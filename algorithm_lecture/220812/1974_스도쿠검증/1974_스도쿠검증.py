import sys
sys.stdin = open('input.txt')
## 실패 ##

T = int(input())
for idx in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]

    for i in lst:
        print(*i)

    flag = False
    print(f'#{idx}', end=' ')
    for i in range(1, 10):
        lst_2 = []
        lst_3 = []
        for j in range(1, 10):

            if j in lst[i-1]:
                pass
            else:
                print(0)
                flag = True
                break

            k = lst[j-1][i-1]
            lst_2.append(k)

            if (i-1) % 3 == 0 and (j-1) % 3 == 0:
                for k in range(3):
                    lst_3.append(lst[i-1+k][j-1])
        print(lst_3)
        lst_3.sort()
        lst_2.sort()

        if (flag):
            break

        if lst_2 == list(range(1, 10)) and lst_3 == list(range(1, 10)):
            pass
        else:
            print(0)
            break
    else:
        print(1)