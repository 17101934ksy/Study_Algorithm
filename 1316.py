import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    p = word[0]

    checker = set()
    c_b = True  
    for w in word:
        if (p != w) and (w in checker):
            c_b = False
            break
        if p != w:
            checker.add(p)
            p = w
    if c_b:
        cnt += 1            
print(cnt)