import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    cnt = 0                         # 괄호의 짝을 확인할 변수
    s = list(input())               # 괄호 입력값
    for i in s:                     # 입력값으로 순회 시작
        if i == '(':                # 괄호가 열리면 cnt + 1
            cnt += 1
        else:                       # 괄호가 닫히면 cnt - 1
            cnt -= 1
        if cnt < 0:                 # cnt가 마이너스가 되면 괄호의 짝이 안맞으므로 break
            print(f'#{idx} -1')
            break
    else:                           # for문이 정상적으로 실행됐을 경우
        if cnt == 0:                # 괄호의 짝이 정상적일 경우
            print(f'#{idx} 1')
        else:                       # 괄호의 짝이 안맞을 경우
            print(f'#{idx} -1')