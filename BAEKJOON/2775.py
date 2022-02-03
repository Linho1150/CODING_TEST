import sys
from collections import deque
que=deque([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]])
for x in range(1,15):
    for y in range(0,15):
        if y==0:
            que.append([1])
        else:
            que[x].append(que[x][y-1]+que[x-1][y])
cnt=int(sys.stdin.readline())

for tmp in range(cnt):
    k=int(sys.stdin.readline().replace('\n',''))
    n=int(sys.stdin.readline().replace('\n',''))
    print(que[k][n-1])
