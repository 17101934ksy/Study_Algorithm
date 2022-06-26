import sys

a, b = map(int, sys.stdin.readline().split())

s = {}
t = []

for _ in range(a):
    s[sys.stdin.readline()] = 0

for _ in range(b):
    k = sys.stdin.readline()

    if k in s.keys():
        s[k] += 1

cnt = 0
for i in s.keys():
    cnt += s[i]

print(cnt)