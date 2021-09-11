import sys
input = sys.stdin.readline 
stack=[]
cnt=input()
for tmp in range(0,int(cnt)):
  number=int(input())
  if number!=0:
    stack.append(number)
  else:
    stack.pop()
print(sum(stack))