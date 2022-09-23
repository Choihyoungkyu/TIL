import sys
sys.stdin = open('input.txt')

for idx in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(12):
        if i%2==0:
            player1.append(cards[i])
        else:
            player2.append(cards[i])
        