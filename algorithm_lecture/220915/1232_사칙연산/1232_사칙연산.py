import sys
sys.stdin = open('input.txt')

def inorder(n):
    if st[n] == '*':
        return inorder(ch1[n]) * inorder(ch2[n])
    elif st[n] == '/':
        return inorder(ch1[n]) / inorder(ch2[n])
    elif st[n] == '+':
        return inorder(ch1[n]) + inorder(ch2[n])
    elif st[n] == '-':
        return inorder(ch1[n]) - inorder(ch2[n])
    else:
        return int(st[n])

for idx in range(1, 11):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    st = [0] * (N+1)
    for _ in range(N):
        lst = list(input().split())
        if len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
            st[int(lst[0])] = lst[1]
        elif len(lst) == 2:
            st[int(lst[0])] = lst[1]
    res = int(inorder(1))
    print(f"#{idx} {res}")
