import sys

a = list(sys.stdin.readline())
a.sort(reverse=True)

print("".join(a[:-1]))
