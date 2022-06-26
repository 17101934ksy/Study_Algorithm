import sys

N = int(input())
g = list(map(str, sys.stdin.readline().rstrip().split()))

M = int(input())
k = list(map(str, sys.stdin.readline().rstrip().split()))

gdict = {}

for i in g:
    if i in gdict.keys():
        gdict[i] += 1
    else:
        gdict[i] = 1

result = [str(gdict[j]) if j in gdict.keys() else str(0) for j in k]

print(" ".join(result))
