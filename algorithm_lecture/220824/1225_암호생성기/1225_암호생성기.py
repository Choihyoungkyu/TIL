# 0.14210s
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = int(input())
    queue = list(map(int, input().split()))
    cnt = 0
    while True:
        cnt %= 5                                # 한 사이클 돌면 cnt가 1부터 다시 시작
        cnt += 1
        if queue[0] - cnt <= 0:                 # 종료 조건
            queue.pop(0)
            queue.append(0)
            break
        else:
            queue.append(queue.pop(0) - cnt)    # 처음 값에 cnt를 빼고 뒤로 보냄
    print(f'#{idx}', end=' ')
    print(*queue)