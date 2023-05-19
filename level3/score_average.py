import sys

n, k = map(int, input().split())

score = list(map(int, input().split()))

average = 0

for i in range(k):
    sum_score = 0

    a, b = map(int, input().split())

    human = b - a + 1
    sum_score = sum(score[a-1:b])
    

    print(f'{sum_score/human : 0.2f}')
