def Bbit_change(s):
    global i
    output = ''
    # 임시 패턴 만들기
    for j in range(6):
        if s[j] == '1':
            output += '1'
        else:
            output += '0'
    # 임시 패턴이 암호 패턴인지 확인
    for k in range(10):
        if output == Patterns[k]:
            print(k, end=' ')
            i += 6
            break
    else:
        i += 1


Patterns = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

T = int(input())
for _ in range(T):
    s = int(input(), 16)
    s = '0' * ((16 - len(bin(s)) + 2)%16) + bin(s).lstrip('0b')
    i = 0
    while i < len(s)-5:
        Bbit_change(s[i:i+6])
# 2
# 0DEC
# 0269FAC9A0

