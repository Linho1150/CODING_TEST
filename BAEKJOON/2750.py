import sys
input=sys.stdin.readline

num=int(input())
tlist=[]
for tmp in range(num):
  inputTmp=input()
  inputTmp=inputTmp.replace('\n','')
  tlist.append(inputTmp)

for tmp1 in range(num):
  for tmp2 in range(tmp1,num):
    if tlist[tmp1]>tlist[tmp2]:
      tmp=tlist[tmp2]
      tlist[tmp2]=tlist[tmp1]
      tlist[tmp1]=tmp

for tmp in range(num):
  print(tlist[tmp])