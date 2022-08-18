import sys

def command(x, s):
    if s[0] == 'push':
        x.append(int(s[1]))

    elif s[0] == 'pop':
        if len(x) == 0:
            print(-1)
        else:
            stack = x.pop()
            print(stack)

    elif s[0] == 'size':
        print(len(x))

    elif s[0] == 'empty':
        if len(x) == 0:
            print(1)
        else:
            print(0)

    elif s[0] == 'top':
        if len(x) == 0:
            print(-1)
        else:
            print(x[-1])

    return x

N = int(input())
x = []
for _ in range(N):
    s = sys.stdin.readline().strip().split()
    x = command(x, s)
