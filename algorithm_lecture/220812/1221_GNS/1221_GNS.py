import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    lst = []
    idx, len_s = map(str, input().split())
    b = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    s = list(map(str, input().split()))
    for i in range(len(b)):
        for j in range(int(len_s)):
            if s[j] == b[i]:
                lst.append(s[j])

    print(idx)
    print(' '.join(lst))