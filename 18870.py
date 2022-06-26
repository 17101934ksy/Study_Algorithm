import sys

N = int(input())
a = list(map(int, sys.stdin.readline().split()))

b = a.copy()
b.sort()
t = {}

cnt = 0
t[b[0]] = 0
for i in range(1, len(b)):
    if b[i] > b[i-1]:
        cnt += 1
    t[b[i]] = cnt

cnt = 0
for i in a:
    b[cnt] = str(t[i])
    cnt += 1

print(" ".join(b))
