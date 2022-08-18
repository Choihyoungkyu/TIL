# 0.13655s
import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    N, s = map(str, input().split())
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:                  # window에 중복값이 있으면
            s = s.replace(s[i:i+2], '')     # 중복값 제거
            if i != 0:                      # index가 0이 아니면
                i -= 1
        else:                               # window에 중복값이 없으면
            i += 1                          # window 이동
    print(f'#{idx} {s}')