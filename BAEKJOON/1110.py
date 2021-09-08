count=0
strNum=input()
target=strNum
while True:
        count=count+1
        sumNum=''
        if int(strNum)<10:
                sumNum=int(strNum)
                if sumNum< 10:
                        sumNum=str(sumNum)+str(sumNum)  #0+5=5
                else:
                        sumNum=strNum+str(sumNum)[1]
        else:
                sumNum=int(strNum[0])+int(strNum[1])
                if sumNum < 10:
                        sumNum=strNum[1]+str(sumNum)
                else:
                        sumNum=strNum[1]+str(sumNum)[1]
        
        strNum=sumNum
        answer=sumNum
        
        if int(answer)<10:
                answer=str(int(answer))
        if answer==target:
                print(count)
                break
