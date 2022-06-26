import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nset = set()
mlist = []

for _ in range(N):
    t = sys.stdin.readline().rstrip()
    nset.add(t)

for _ in range(M):
    k = sys.stdin.readline().rstrip()
    if k in nset:
        mlist.append(k)
        
mlist.sort()
print(len(mlist))
for i in mlist:
    print(i)


