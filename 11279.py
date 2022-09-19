import sys
from heapq import heappush, heappop
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    n = int(input())

    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            result = heappop(heap)[-1]
            print(result)
    
    heappush(heap, (-n, n))
    

