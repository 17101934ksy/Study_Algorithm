T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().strip().split()))
    queue = [(v, idx) for idx, v in enumerate(queue)]
    count = 0

    while True:
        if max(queue)[0] == queue[0][0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))