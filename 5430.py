import sys
from collections import deque

for _ in range(int(input())):
    command = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    num_list = sys.stdin.readline().strip()[1:-1].split(',')
    if num_list != ['']:
        num_list = deque(map(int, num_list))
    else:
        num_list = deque([])
    
    break_false, direction = True, True
    R_cnt = 0

    for ch in command:
        if ch == 'R':
            R_cnt += 1
            if direction:
                direction = False
            else:
                direction = True

        elif ch == 'D':
            if len(num_list) == 0:
                print('error')
                break_false = False
                break

            if direction:
                num_list.popleft()
            else:
                num_list.pop()

    if break_false:
        if R_cnt % 2 == 0:
            print('[', end='')
            print(*num_list, sep=',', end='')
            print(']')
        else:
            print('[', end='')
            print(*list(num_list)[::-1], sep=',', end='')
            print(']')
