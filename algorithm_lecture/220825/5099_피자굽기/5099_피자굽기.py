# 0.13178s
import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = []                                  # 피자
    num = []                                    # 피자의 넘버
    i = 0                                       # 피자의 넘버를 부여할 변수
    while True:
        if len(queue) != N and len(lst) != 0:   # 순서대로 피자를 넣음 (한 피자가 끝났을 때 남은 피자도 넣음)
            i += 1
            num.append(i)
            queue.append(lst.pop(0))
        else:
            if queue[0]//2 != 0:                # 피자가 다 안녹았으면 계속 돌림
                queue.append(queue.pop(0)//2)
                num.append(num.pop(0))
            else:                               # 다녹았으면 빼냄
                queue.pop(0)
                num.pop(0)
                if len(queue) == 1:             # 화덕 내 피자의 수가 1이 된다면 break하고 그 피자의 번호를 출력
                    print(f'#{idx} {num[0]}')
                    break