cnt,money=list(map(int,input().split()))
layerList=[]
count=0
for tmp in range(cnt):
    layerList.append(int(input()))
    
layerList=layerList[::-1]
for tmp in range(len(layerList)):
    if layerList[tmp]<=money:
        count=count+(money//layerList[tmp])
        money=money-((money//layerList[tmp])*layerList[tmp])
print(count)