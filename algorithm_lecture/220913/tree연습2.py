'''
정점 번호 V : 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

def f(n):                       # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:                  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)

# 자식을 인덱스로 부모 번호 저장
par = [0]*(V + 1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:             # 아직 자식이 없으면
        ch1[p] = c              # 자식1로 저장
    else:                       # 자식이 있으면
        ch2[p] = c              # 자식 2로 저장

# root = 3 의 자손의 수
print(f'root = 3의 자손의 수 : {f(3)}')

# root = 1 의 자손의 수
print(f'root = 1의 자손의 수 : {f(1)}')