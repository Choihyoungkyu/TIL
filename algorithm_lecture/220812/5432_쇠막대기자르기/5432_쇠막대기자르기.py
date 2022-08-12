import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    '''
    #1 ()(((()())(())()))(())
    #2 (((()(()()))(())()))(()())
    '''
    s = input()
    lod = []
    cnt = 0
    tot = 0
    for i in range(len(s)):
        if s[i] == '(' and s[i:i+2] != '()' and 0<=i<len(s)-1:
            lod.append(1)
            cnt += 1
        elif s[i] == ')' and s[i-1:i+1] != '()' and 1<=i<len(s):
            cnt -= 1

        if s[i:i+2] == '()' and 0<=i<len(s)-1:
            for j in range(cnt):
                lod[j] += 1
    print(f'#{idx} {sum(lod)}')