import sys
from collections import deque

stack=deque()
result=deque()
cnt=int(sys.stdin.readline())
listInt=[a for a in range(cnt,0,-1)]

for tmp in range(cnt):
    target=int(sys.stdin.readline())
    if len(listInt)!=0:
        while listInt[-1] <= target:
            stack.append(listInt.pop())
            result.append('+')
            if len(listInt)==0:
                break
    
    if stack[-1]==target:
        stack.pop()
        result.append('-')
    else:
        result=["NO"]
        break
for tmp in range(len(result)):
    print(result[tmp])