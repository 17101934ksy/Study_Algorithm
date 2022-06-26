import sys

N = int(input())
s = 0
num = [0] * (8001)
cnt = [0] * (8001)

num_min = 4001
num_max = -4001

c = 0

for i in range(N):
    a = int(sys.stdin.readline())
    s += a
    num[a+4000] = a
    cnt[a+4000] += 1
    
    if a <= num_min:
        num_min = a
    if a >= num_max:
        num_max = a

print(f'{round(s/N)}')

t = 0
for idx, k in enumerate(cnt):
    c += k
    if c >= (N+1)/2:
        t = idx
        break
print(num[t])

max_ = []
m = max(cnt)

for idx, i in enumerate(cnt):
    if i == m:
        max_.append(num[idx])

max_.sort()
if len(max_) > 1:
    print(max_[1])
else:
    print(max_[0])

print(num_max - num_min)

