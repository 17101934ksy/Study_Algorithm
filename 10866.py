import sys
from collections import deque

deck = deque([])

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline()
    
    if len(s.split()) == 1:
        c = s.split()[0]
    else:
        c, x = s.split()
        x = int(x)

    if c == 'push_front':
        deck.appendleft(x)
    
    elif c == 'push_back':
        deck.append(x)

    elif c == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])

    elif c == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])

    elif c == 'size':
        print(len(deck))

    elif c == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)

    elif c == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.popleft())

    elif c == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())
 
    

