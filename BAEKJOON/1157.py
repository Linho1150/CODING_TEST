inputStr=input()
inputStr=inputStr.lower()
inputDic={}
listDic=[]
maxInt=0
for tmp in inputStr:
    if tmp in inputDic.keys():
        inputDic[tmp]=inputDic[tmp]+1
    else:
        inputDic[tmp]=1

for tmp in inputDic.keys():
    valMax=inputDic[tmp]
    if maxInt<valMax:
        maxInt=valMax
        listDic=[]
        listDic.append(tmp.upper())
    elif maxInt==valMax:
        listDic.append(tmp.upper())

if len(listDic)==1:
    print(listDic[0])
elif len(listDic)>1:
    print("?")