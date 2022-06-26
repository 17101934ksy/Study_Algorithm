import sys
from collections import Counter

a, b = [], []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)

x = Counter(a).most_common()[1][0]
y = Counter(b).most_common()[1][0]
print(x, y)



