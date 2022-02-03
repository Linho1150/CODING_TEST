import sys
from collections import deque

cnt=int(sys.stdin.readline())
que=deque()
def empty():
    if len(que)==0:
        return 1
    else:
        return 0
result=deque()
for tmp in range(cnt):
    inputTxt=sys.stdin.readline()
    if 'push_back' in inputTxt:
        a,b=inputTxt.split()
        que.append(int(b))
    elif 'push_front' in inputTxt:
        a,b=inputTxt.split()
        que.appendleft(int(b))
    elif 'pop_front' in inputTxt:
        if empty():
            result.append(-1)
        else:
            result.append(que.popleft())
    elif 'pop_back' in inputTxt:
        if empty():
            result.append(-1)
        else:
            result.append(que.pop())
    elif 'size' in inputTxt:
        result.append(len(que))
    elif 'empty' in inputTxt:
        if empty():
            result.append(1)
        else:
            result.append(0)
    elif 'front' in inputTxt:
        if empty():
            result.append(-1)
        else:
            result.append(que[0])
    elif 'back' in inputTxt:
        if empty():
            result.append(-1)
        else:
            result.append(que[-1])

for tmp in result:
    print(tmp)