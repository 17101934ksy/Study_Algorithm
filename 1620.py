import sys

N, M = map(int, sys.stdin.readline().split())

t = {}
p = []

for i in range(N):
    k = sys.stdin.readline().rstrip()
    t[k] = i+1
    p.append(k)

for _ in range(M):
    qna = sys.stdin.readline().rstrip()
    if qna.isdigit():
        print(p[int(qna)-1])

    else:
        print(t[qna])
