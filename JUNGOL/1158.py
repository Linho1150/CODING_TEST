numList=input().split()

def swap(a,b):
  a,b=b,a

for tmp in range(len(numList)):
  key=tmp+1
  for tmp2 in range(key-1,0,-1):
    if key<numList[tmp2]:
      swap(key,numList[tmp])
      break
    elif numList[tmp2]<numList[tmp2-1]:
      swap(numList[tmp2],numList[tmp2-1])
  print(numList)
