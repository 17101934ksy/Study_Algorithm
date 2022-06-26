import sys

N = int(input())
s = [0]*2000000
cnt = -1

for i in range(N):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        num = int(a[1])
        s[cnt] = num
        cnt -= 1 

    elif a[0] == 'pop':
        if s[-1] == 0:
            print(-1)
        else:
            print(s.pop())
            cnt += 1

    elif a[0] == 'front':
        if s[-1] == 0:
            print(-1)
        else:
            print(s[-1])

    elif a[0] == 'back':
        if s[-1] == 0:
            print(-1)
        elif s[-2] == 0:
            print(s[-1])
        else:
            print(s[cnt+1])

    elif a[0] == 'size':
        print(abs(cnt+1))

    elif a[0] == 'empty':
        if s[-1] == 0:
            print(1)
        else:
            print(0)
    


