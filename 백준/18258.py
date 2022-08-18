from collections import deque
import sys

queue = deque()
N = int(input())

input = sys.stdin.readline

for i in range(N):
    string = list(map(str,input().split()))
    order = string[0]
    if order == 'push':
        queue.append(string[1])
    elif order == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    elif order == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif order == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif order == 'size':
        print(len(queue))