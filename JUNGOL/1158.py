num=input()
numList=input().split()

for tmp in range(len(numList)):
  key=tmp+1
  if key>len(numList)+1:
    break
  else:
    for tmp2 in range(len(numList)-1,-1,-1):
      print(tmp2,end=' ')
      if numList[tmp2]>numList[key]:
        numList[key],numList[tmp]=numList[tmp],numList[key]
  print(numList)