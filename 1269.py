import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

aset = set(map(int, sys.stdin.readline().rstrip().split()))
bset = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(aset ^ bset))