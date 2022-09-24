'''
1
32888 2
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''
T = int(input())
for idx in range(1, T+1):
    s, n = input().split()
    S = list(map(int, s))
    n = int(n)
    i = 0
    cnt = 0
    while cnt < n:
        if i >= len(S):
            S[-1], S[-2] = S[-2], S[-1]
            cnt += 1
        else:
            maxV = S[i]
            tmp = i
            for j in range(i, len(S)):
                if maxV <= S[j]:
                    maxV = S[j]
                    tmp = j
            if tmp != i:
                S[i], S[tmp] = S[tmp], S[i]
                cnt += 1
            for j in range(len(S)-1, len(S)-1-i, -1):
                if S[j] > S[j-1]:
                    S[j], S[j-1] = S[j-1], S[j]
            i += 1

    print(f'#{idx}', end=' ')
    for i in range(len(S)):
        print(S[i], end='')
    print()