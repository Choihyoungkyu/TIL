import sys
import time
from datetime import timedelta

start = time.time()
sys.stdin = open('input.txt')

N = int(input())  # N번 입력을 받겠다
for _ in range(N):
    y = int(input())  # y줄을 입력 받겠다
    num = list(map(int, input().split()))
    count = []
    for i in range(y):
        cnt = 0
        for j in range(i+1, y):
            if num[i] > num[j]:
                cnt += 1
        count.append(cnt)
    print(max(count))

end = time.time()
print(f"Time elapsed : {(end - start):.3f}s")
