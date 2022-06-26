import sys

N = int(input())
t = []
for n in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    t.append(a)

t.sort(key=lambda x: (x[1], x[0]))

for i in t:
    print(i[0], i[1])

