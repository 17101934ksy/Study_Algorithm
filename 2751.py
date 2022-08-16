import sys

N = int(sys.stdin.readline())
s = [True] * 2000001


for _ in range(N):
    a = int(sys.stdin.readline())
    s[a+1000000] = a

for i in s:
    if type(i) == int:
        print(i)
