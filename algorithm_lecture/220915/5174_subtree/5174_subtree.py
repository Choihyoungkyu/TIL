import sys
sys.stdin = open('input.txt')

# 중위순회
def inorder(n):
    global cnt
    if n:
        inorder(ch1[n])     # 왼쪽 자식으로 재귀
        cnt += 1            # 카운트 한개 올림
        inorder(ch2[n])     # 오른쪽 자식으로 재귀


T = int(input())
for idx in range(1, T+1):
    E, N = map(int, input().split())
    ch1 = [0] * (E+2)       # 왼쪽 자식 리스트
    ch2 = [0] * (E+2)       # 오른쪽 자식 리스트
    lst = list(map(int, input().split()))
    # 자식 리스트 채우기
    for i in range(0, 2*E, 2):
        a, b = lst[i], lst[i+1]
        if ch1[a] == 0:
            ch1[a] = b
        else:
            ch2[a] = b
    cnt = 0
    inorder(N)
    print(f'#{idx} {cnt}')