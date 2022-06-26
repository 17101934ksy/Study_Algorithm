import sys

N = int(input())
n = []

for i in range(N):
    a = sys.stdin.readline().split()
    n.append([int(a[0]), a[1], i])

n.sort(key=lambda x: (x[0], x[2]))

for i in n:
    print(i[0], i[1])