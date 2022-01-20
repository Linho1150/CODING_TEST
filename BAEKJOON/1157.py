inputStr=input()
inputStr=inputStr.lower()
inputDic={}
for tmp in inputStr:
    if tmp in inputDic:
        inputDic[tmp]=1
    else:
        inputDic[tmp]=inputDic[tmp]+1
