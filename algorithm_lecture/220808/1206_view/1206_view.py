import sys
import time
from datetime import timedelta

start = time.time()
sys.stdin = open('input.txt')

for idx in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        a = lst[i] - lst[i-2]
        b = lst[i] - lst[i-1]
        c = lst[i] - lst[i+1]
        d = lst[i] - lst[i+2]
        minV = min(a, b, c, d)
        if minV > 0:
            cnt += minV
        # if a > 0 and b > 0 and c > 0 and d > 0:
        #     cnt += min(a, b, c, d)
    print(f'#{idx+1} {cnt}')

end = time.time()
print(f"Time elapsed : {(end - start):.3f}s")