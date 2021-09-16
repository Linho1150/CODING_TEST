num=int(input())
for tmp1 in range(num):
  total=0
  avg=0
  cnt=0
  mlist=map(int,input().split())
  mlist=list(mlist)
  for tmp2 in range(1,mlist[0]+1):
    total=total+mlist[tmp2]
  avg=total/mlist[0]
  for tmp3 in range(1,mlist[0]+1):
    if mlist[tmp3] > avg:
      cnt=cnt+1
  print("{:.3f}".format((cnt/mlist[0])*100)+'%')
