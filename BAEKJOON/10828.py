import sys
input = sys.stdin.readline 
stack=[]
cnt=input()
for tmp in range(0,int(cnt)):
  num=input()
  if 'push' in num:
    a,b=num.split(' ')
    stack.append(b)
  elif 'top' in num:
    try:
      print(stack[len(stack)-1],end='')
    except:
      print(-1)
      continue
  elif 'size' in num:
    print(len(stack))
  elif 'empty' in num:
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif 'pop' in num:
    try:
      print(stack.pop(),end='')
    except:
      print(-1)
      continue