import sys

K = int(input())
x = []

def stack(x, d):
    if d == 0:
        x.pop()
    else:
        x.append(d)
    return x

for _ in range(K):
    x = stack(x, int(sys.stdin.readline().strip()))

print(sum(x))

