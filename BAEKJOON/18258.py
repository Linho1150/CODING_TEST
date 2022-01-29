from collections import deque
import sys
deque=deque()
def empty():
    if len(deque)==0:
        return 1
    else:
        return 0

cnt=int(sys.stdin.readline())
for tmp in range(cnt):
    work=sys.stdin.readline()
    if 'push' in work:
        a,b=work.split()
        deque.append(b)
    elif 'empty' in work:
        if empty():
            print(1)
        else:
            print(0)
            
    elif 'pop' in work:
        if empty():
            print(-1)
        else:
            print(deque.popleft())
    elif 'size' in work:
        print(len(deque))
    elif 'front' in work:
        if empty():
            print(-1)
        else:
            print(deque[0])
    elif 'back' in work:
        if empty():
            print(-1)
        else:
            print(deque[-1])