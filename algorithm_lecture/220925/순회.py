'''
정점 번호 V : 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i

E = 4
arr = [1, 2, 1, 3, 3, 4, 3, 5]
V = E + 1
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

root = find_root(V)
print(f'root : {root}')
print()

print('전위순회')
preorder(root)
print()

print('중위순회')
inorder(root)
print()

print('후위순회')
postorder(root)
print()
