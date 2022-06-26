import sys
N = int(input())
s = []

for i in range(N):
    s.append(list(map(int , sys.stdin.readline().split())))

s.sort()

for i in s:
    print(i[0], i[1])