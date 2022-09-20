def Bbit_change(i):
    output = 0
    for j in range(7):
        if j < len(i) and i[j] == '1':
            output += 2**(len(i)-1-j)
    print(output, end=' ')

T = int(input())
for _ in range(T):
    s = int(input(), 16)
    s = '0' * (24-len(bin(s))+2) + bin(s).lstrip('0b')
    for i in range(0, len(s), 7):
        Bbit_change(s[i:i+7])
    print()

# 2
# 0F97A3
# 01D06079861D79F99F

