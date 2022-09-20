def Bbit_change(i):
    output = 0
    for j in range(7):
        if i[j] == '1':
            output += 2**(6-j)
    print(output, end=' ')

T = int(input())
for _ in range(T):
    s = input()
    for i in range(0, len(s), 7):
        Bbit_change(s[i:i+7])
    print()
