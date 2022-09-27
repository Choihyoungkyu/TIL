import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    low_lst = merge_sort(lst[:middle])
    high_lst = merge_sort(lst[middle:])

    merged_lst = []
    l = h = 0
    if low_lst[-1] > high_lst[-1]:
        cnt += 1
    while l < len(low_lst) and h < len(high_lst):
        if low_lst[l] < high_lst[h]:
            merged_lst.append(low_lst[l])
            l += 1
        else:
            merged_lst.append(high_lst[h])
            h += 1
    merged_lst += low_lst[l:]
    merged_lst += high_lst[h:]
    return merged_lst

for idx in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    print(f'#{idx}', end=' ')
    print(merge_sort(lst)[N//2], cnt)