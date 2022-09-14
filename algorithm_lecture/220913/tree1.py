'''
정점 번호 V : 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

# 전위순회
def preorder(n):
    if n:
        print(n, end=' ')        # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')        # visit(n)
        inorder(ch2[n])

# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')        # visit(n)

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
# root = 1
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
# print(ch1, ch2)


# 루트 찾기
root = find_root(V)
print(f'root : {root}')
print()

# 전위순회
print('전위순회')
preorder(root)
print()
print()

# 중위순회
print('중위순회')
inorder(root)
print()
print()

# 후위순회
print('후위순회')
postorder(root)
