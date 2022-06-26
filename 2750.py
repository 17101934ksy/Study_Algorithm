import sys
N = int(input())
t = []

for n in range(N):
    a = int(sys.stdin.readline())
    t.append(a)

t.sort()

for i in t:
    print(i)
