import sys

N, k = map(int, sys.stdin.readline().strip().split())
x = list(map(int, sys.stdin.readline().strip().split()))

x.sort(reverse=True)

print(x[k-1])