import sys
sys.stdin = open('input.txt')

T = int(input())
# 방법 1
# for idx in range(1, T+1):
#     s = input()
#     print(f'#{idx} {s[::-1]}')

# 방법 2
for idx in range(1, T+1):
    s = input()
    lst = list(map(str, s))
    for i in range(len(s)//2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    print(f'#{idx}', end=' ')
    print(''.join(lst))