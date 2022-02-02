from collections import deque
import sys

cnt=int(sys.stdin.readline())
que=deque()
middle=0

for tmp in range(cnt):
    que.append(int(sys.stdin.readline()))

a=list(que)
a.sort()
for tmp in range(len(a)):
    print(a[tmp])