import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    A = input()                             # 찾을 문자열
    B = input()                             # 전체 문자열
    cnt = 0                                 # 찾은 개수
    for i in range(len(B) - len(A) + 2):    # BruteForce 시작
        for j in range(len(A)):
            if B[i + j] == A[j]:            # 한글자씩 비교해서 똑같으면 패스
                pass
            else:                           # 다르면 다음 순서로 넘어감
                break
        else:                               # 각 글자가 다 같으면 찾은 개수 +1
            cnt += 1
    print(f'#{idx} {cnt}')