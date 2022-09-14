import sys
import time
from datetime import timedelta

start = time.time()
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    num = [0] * 10  # 0~9 빈 리스트 생성
    s = input()
    for i in s:  # 받은 문자열의 숫자의 개수만큼 리스트 num에 할당
        num[int(i)] += 1
    j = 0
    triplet = run = 0
    while j < 10:  # triplet의 존재부터 확인
        if num[j] >= 3:
            triplet += 1
            num[j] -= 3
            continue
        j += 1
    j = 0
    while j <= 7:  # run의 존재 확인
        if num[j] != 0 and num[j] == num[j+1] == num[j+2]:
            run += 1
            num[j] -= 1
            num[j+1] -= 1
            num[j+2] -= 1
            continue
        j += 1
    print(1) if triplet + run == 2 else print(0)  # baby_gin 확인

end = time.time()
print(f"Time elapsed : {(end - start):.3f}s")