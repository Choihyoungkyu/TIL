import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]
    cnt = 0
    for _ in range(E):
        u, v = map(int, input().split())
        if find_set(u) != find_set(v):
            tmp = find_set(v)
            union(u, v)
            for i in range(V+1):            # 대표노드가 바뀌면 그 하위 노드들을 다 바꾼다
                if rep[i] == tmp:
                    rep[i] = find_set(v)
    res = set(rep)
    print(f'#{tc} {len(res)-1}')