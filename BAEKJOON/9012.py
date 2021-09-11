import sys
input=sys.stdin.readline
cnt=int(input())
mlist=[]
s=0
for _ in range(cnt):
  valStr=input()
  valStr=list(valStr)
  s=0
  for tmp in range(len(valStr)-1):
    if valStr[tmp]=='(':
      s=s+1
    elif valStr[tmp]==')' and s!=0:
      s=s-1
    else:
      s=1
      break
  if s==0:
    print('YES')
  else:
    print('NO')

