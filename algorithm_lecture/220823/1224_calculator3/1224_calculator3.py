# 0.13366s
import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    stack1 = []
    stack2 = []
    res = []
    N = int(input())
    s = list(input())
    num = list(map(str, range(1, 11)))

    for i in range(N):
        if s[i] in num:
            res.append(int(s[i]))
        else:
            if not stack1:
                stack1.append(s[i])
            elif s[i] == '(':
                stack1.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                while stack1 and stack1[-1] != '(' and stack1[-1] != '+' and stack1[-1] != '-':
                    res.append(stack1.pop())
                stack1.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while stack1 and stack1[-1] != '(':
                    res.append(stack1.pop())
                stack1.append(s[i])
            elif s[i] == ')':
                while stack1 and stack1[-1] != '(':
                    res.append(stack1.pop())
                stack1.pop()
    while stack1:
        res.append(stack1.pop())

    for i in range(len(res)):
        if str(res[i]) in num:
            stack2.append(res[i])

        elif res[i] == '*':
            tmp = stack2.pop() * stack2.pop()
            stack2.append(tmp)
        elif res[i] == '/':
            tmp = 1 / (stack2.pop() / stack2.pop())
            stack2.append(tmp)
        elif res[i] == '+':
            tmp = stack2.pop() + stack2.pop()
            stack2.append(tmp)
        elif res[i] == '-':
            tmp = stack2.pop() - stack2.pop()
            stack2.append(-tmp)

    print(f'#{idx} {tmp}')