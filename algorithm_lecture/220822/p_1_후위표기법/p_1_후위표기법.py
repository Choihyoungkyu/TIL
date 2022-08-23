import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    stack = []
    res = []
    s = list(input())
    for i in s:
        if i == '+' or i == '-' or i == '*' or i == '/':
            stack.append(i)
        else:
            res.append(i)
    for _ in range(len(stack)):
        res.append(stack.pop())
    print(f'#{idx}', end=' ')
    print(''.join(res))