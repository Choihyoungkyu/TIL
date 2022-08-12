import sys
sys.stdin = open('input.txt')

idx = 1
while True:
    try:
        num = int(input())
        n = abs(num)
        str_ = ''
        if n == 0:
            print(f'#{idx} 0 {type(str_)}')
        else:
            while n > 0:
                k = n % 10
                n = n // 10
                str_ = chr(48 + k) + str_
            if num > 0:
                print(f'#{idx} {str_} {type(str_)}')
            else:
                print(f'#{idx} -{str_} {type(str_)}')
        idx += 1
    except:
        break