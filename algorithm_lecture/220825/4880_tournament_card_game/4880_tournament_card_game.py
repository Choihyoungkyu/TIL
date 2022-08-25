# 0.13835s
import sys
sys.stdin = open('input.txt')

# 1 : 가위, 2 : 바위, 3 : 보
def f(lst1, lst2, num1, num2):
    if lst1 == 1 and lst2 == 2:
        stack.append(lst2)
        stack_num.append(num2)
    elif lst1 == 1 and lst2 == 3:
        stack.append(lst1)
        stack_num.append(num1)
    elif lst1 == 2 and lst2 == 1:
        stack.append(lst1)
        stack_num.append(num1)
    elif lst1 == 2 and lst2 == 3:
        stack.append(lst2)
        stack_num.append(num2)
    elif lst1 == 3 and lst2 == 1:
        stack.append(lst2)
        stack_num.append(num2)
    elif lst1 == 3 and lst2 == 2:
        stack.append(lst1)
        stack_num.append(num1)
    else:
        stack.append(lst1)
        stack_num.append(num1)

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split()))]
    num = [list(range(1, N+1))]

    while True:
        for i in range(len(lst)):
            stack = []
            stack_num = []
            if len(lst[i]) == 2:
                f(lst[i][0], lst[i][1], num[i][0], num[i][1])
                lst[i] = stack
                num[i] = stack_num
            elif len(lst[i]) % 2 == 1:
                lst[i] = [lst[i][0:(len(lst)+1)//2], lst[i][(len(lst)+1)//2:]]
                num[i] = [num[i][0:(len(num)+1)//2], num[i][(len(num)+1)//2:]]

            else:
                for j in range(0, len(lst[i]), 2):
                    f(lst[i][j], lst[i][j+1], num[i][j], num[i][j+1])
                lst[i] = stack
                num[i] = stack_num
        if len(lst) == 1:
            break

    print(f'#{idx} {num[-1]}')