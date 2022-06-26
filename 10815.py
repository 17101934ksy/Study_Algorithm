import sys

N = int(input())
fst = list(map(int, sys.stdin.readline().split()))

K = int(input())
sec = list(map(int, sys.stdin.readline().split()))

dict1 = {sec[i]: 0 for i in range(len(sec))}

for i in range(N):
    if fst[i] in dict1.keys():
        dict1[fst[i]] += 1

print(" ".join(map(str, list(dict1.values()))))