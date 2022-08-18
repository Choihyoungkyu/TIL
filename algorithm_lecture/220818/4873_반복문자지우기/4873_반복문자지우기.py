# 0.13908s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    s = input()
    i = 0
    while True:
        if len(s)-1 > i and i >= 0:             # window가 이동하면서 연속한 두 문자를 비교
            if s[i] == s[i+1]:                  # 같으면 공백으로 바꿈
                s = s.replace(s[i:i+2], '')
                i -= 1                          # 지운 후 떨어져있던 문자가 붙은 후 다시 확인하기 위해
            else:
                i += 1

        elif i < 0:                             # 처음에 반복문자가 나오면 i가 -1이 되기 때문에 예외 케이스 넣음
            i += 1
            if s[i] == s[i+1]:
                s = s.replace(s[i:i+2], '')
                i -= 1
            else:
                i += 1
        else:                                   # 다 돌면 break
            break
    print(f'#{idx} {len(s)}')