from collections import deque
import sys

cnt=int(sys.stdin.readline())
que=deque()
for tmp in range(1,cnt+1):
    que.append(tmp)
    
for tmp in range(cnt-1):
        que.popleft()
        que.append(que.popleft())
print(que[0])