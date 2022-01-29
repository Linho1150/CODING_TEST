import sys
class queue:
    def __init__(self):
        self.listqueue=[]
        self.cnt=0
        
    def push(self,val):
        self.listqueue.append(val)
        return
    
    def pop(self):
        if self.empty():
            return -1
        else:
            tmp=self.listqueue[self.cnt]
            self.cnt=self.cnt+1
            return tmp
            
    def size(self):
        return len(self.listqueue)-self.cnt
        
    def empty(self):
        if len(self.listqueue)-self.cnt==0:
            return 1
        else:
            return 0
            
    def front(self):
        if self.empty():
            return -1
        else:
            return self.listqueue[self.cnt]
            
    def back(self):
        if self.empty():
            return -1
        else:
            return self.listqueue[len(self.listqueue)-1-self.cnt]
            
cnt=int(input())
que=queue()
for tmp in range(cnt):
    a=sys.stdin.readline()
    if "push" in a:
        b,c=a.split()
        que.push(c)
    elif "pop" in a:
        print(que.pop())
    elif "size" in a:
        print(que.size())
    elif "empty" in a:
        print(que.empty())
    elif "front" in a:
        print(que.front())
    elif "back" in a:
        print(que.back())
    
    
        
        