numList=list(map(int,input().split()))


for tmp in range(len(numList)):
  key=tmp+1
  if key==len(numList):
    break
  for tmp2 in range(key-1,0,-1):
    print(numList[key],numList[tmp2])
    if numList[key]<numList[tmp2]:
      numList[key],numList[tmp2]=numList[tmp2],numList[key]
      break
    elif numList[tmp2]>numList[tmp2-1]:
      numList[tmp2-1],numList[tmp2]=numList[tmp2],numList[tmp2-1]
    print(numList)
  