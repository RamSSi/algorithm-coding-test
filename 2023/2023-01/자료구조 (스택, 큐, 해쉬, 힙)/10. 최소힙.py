import sys
import heapq as hq

input = sys.stdin.readline

a = []

while True:
    n = int(input().strip())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
