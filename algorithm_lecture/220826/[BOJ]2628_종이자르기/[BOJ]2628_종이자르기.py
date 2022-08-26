import sys
input = lambda : sys.stdin.readline().strip()
# sys.stdin = open('input.txt')

N, M = map(int, input().split())
K = int(input())
dic = {0:[], 1:[]}
for _ in range(K):
    a, b = map(int, input().split())
    dic[a].append(int(b))
dic[0].append(M)
dic[1].append(N)
dic[0].sort()
dic[1].sort()

x=y=0
maxX=maxY=0

for i in dic[0]:
    if i-x > maxX:
        maxX = i-x
    x = i
for j in dic[1]:
    if j-y > maxY:
        maxY = j-y
    y = j
print(maxX*maxY)
