import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')

for _ in range(10):
    idx = int(input())
    key = input()
    s = input()
    cnt = 0
    for i in range(len(s)-len(key)+1):
        for j in range(len(key)):
            if s[i+j] == key[j]:
                pass
            else:
                break
        else:
            cnt += 1
    else:
        print(f'#{idx} {cnt}')