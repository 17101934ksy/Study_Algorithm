import sys

N = int(input())
n = [set() for _ in range(50)]

for i in range(N):
    a = sys.stdin.readline().split()
    k = len(a[0])-1
    n[k].add(a[0])

for j in n:
    if len(j) != 0:
        j = list(j)
        j.sort()
        for t in j:
            print(t)
