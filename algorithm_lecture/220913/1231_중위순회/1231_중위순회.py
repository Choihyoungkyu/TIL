import sys
sys.stdin = open('input.txt')

def inorder(n):                             # 중위순회
    if n:
        inorder(ch1[n])
        print(st[n], end='')
        inorder(ch2[n])

for idx in range(1, 11):
    K = int(input())                        # 노드 수
    ch1 = [0] * (K+1)                       # 왼쪽 자식 리스트
    ch2 = [0] * (K+1)                       # 오른쪽 자식 리스트
    st = [0] * (K+1)                        # 문자열 리스트
    for i in range(K):
        lst = list(input().split())         # 입력 리스트

        if len(lst) == 4:                   # 리스트 길이가 4이면 (= 자식이 둘 다 있으면)
            ch1[int(lst[0])] = int(lst[2])  # 왼쪽 자식 입력
            ch2[int(lst[0])] = int(lst[3])  # 오른쪽 자식 입력
            st[int(lst[0])] = lst[1]        # 문자열 입력

        elif len(lst) == 3:
            ch1[int(lst[0])] = int(lst[2])
            st[int(lst[0])] = lst[1]

        elif len(lst) == 2:
            st[int(lst[0])] = lst[1]

    print(f'#{idx}', end=' ')               # 출력
    inorder(1)
    print()

