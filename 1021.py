import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque(range(1, N+1))

s = list(map(int, sys.stdin.readline().split()))    

result = 0
for i in s:
    cnt = 0
    if q[0] == i:
        q.popleft()

    else:
        for j in q:
            if j == i:
                break
            cnt += 1
        if cnt <= len(q) / 2:
            for c in range(cnt):
                result += 1
                q.append(q.popleft())
            q.popleft()
        else:
            for c in range(len(q) - cnt):
                result += 1
                q.appendleft(q.pop())
            q.popleft()
             
print(result)