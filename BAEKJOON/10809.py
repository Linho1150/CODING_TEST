strInput=input()
tmpList=[-1]*(ord('z')-ord('a')+1)
for tmp in range(len(strInput)):
    cnt=ord(strInput[tmp])-ord('a')
    tmpWord=tmpList[cnt]
    if tmpWord == -1:
        tmpList[cnt]=tmp

result=' '.join(map(str,tmpList))
print(result)