import sys

K, P, N = map(int, input().split())

print(K*pow(P, N, 1000000007)%1000000007)
