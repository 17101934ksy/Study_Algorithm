import sys

s = sys.stdin.readline().rstrip()
t = set()


for i in range(len(s)):
    for j in range(i, len(s)):
        k = s[i:j+1]
        t.add(k)

print(len(t))

