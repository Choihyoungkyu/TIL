
def f(n):
    if not n:
        return 0
    L = f(ch1[n])
    R = f(ch2[n])
    return L+R+1

E = 4
arr = [1, 2, 1, 3, 3, 4, 3, 5]
V = E + 1
root = 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

print(f'root = 1의 자손의 수 : {f(1)}')