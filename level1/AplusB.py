import sys

test = int(input())

result = 0

for i in range(test):
    a, b = map(int, input().split())

    result = a + b

    print(f'Case #{i+1}: {result}')
