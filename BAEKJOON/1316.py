inputTxt=int(input())
cnt=0
for tmp in range(inputTxt):
    tmpList=[]
    inputStr=list(input())
    priview=""
    boool=True
    
    ##한글자씩 들어간다.
    for tmpword in inputStr:
        if priview=="":
            priview=tmpword
            
        if tmpword in tmpList and tmpword!=priview:
            boool=False
            break
        else:
            priview=tmpword
            tmpList.append(tmpword)
            
    if boool:
        cnt=cnt+1
print(cnt)
    
