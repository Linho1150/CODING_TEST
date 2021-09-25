num=int(input())
cnt=0
total=0
mlist=[]
for tmp in range(num):
  tmpTxt=input()
  tmpList=list(tmpTxt)
  total=0
  cnt=0
  for tmp1 in range(len(tmpTxt)):
    if tmpList[tmp1]=='O':
      cnt=cnt+1
      total=total+cnt
    else:
      cnt=0
  print(total)


