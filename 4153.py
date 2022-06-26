import sys

while True:
    s = sys.stdin.readline().rstrip()

    if s == "0 0 0":
        break
    
    a = list(map(int, s.split()))
    a.sort()

    if a[0]**2 + a[1]**2  == a[2]**2:
        print('right')
    else:
        print('wrong')