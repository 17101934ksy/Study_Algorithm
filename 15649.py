import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def dsf():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return 
    
    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        dsf()
        s.pop()
dsf()       