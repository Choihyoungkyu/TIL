import sys
sys.stdin = open('input.txt')

def binarySearch(e, k, s=1):
    cnt = 0
    while s <= e:
        c = int((s + e) / 2)                # 중간값 설정
        cnt += 1                            # 카운트 증가
        if c == k:                          # 검색 성공
            return cnt                      # 카운트 반환
        elif c > k:                         # 중간값이 목표값보다 크면
            e = c                           # end를 중간값으로 설정
        else:                               # 중간값이 목표값보다 작으면
            s = c                           # start를 중간값으로 설정
    return -1                               # 검색 실패

T = int(input())
for idx in range(1, T+1):
    P, Pa, Pb = map(int, input().split())   # P : 전체 페이지, Pa : A의 목표값, Pb : B의 목표값
    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)
    if A < B:
        print(f'#{idx} A')
    elif A > B:
        print(f'#{idx} B')
    else:
        print(f'#{idx} 0')

