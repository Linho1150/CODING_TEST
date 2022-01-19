def divide(i):
    tmp=len(str(i))
    if(tmp==4):
        return (i//1000)+((i//100)-(i//1000)*10)+((i//10)-(i//100)*10)+(i%10)+i
    elif(tmp==3):
        return (i//100)+(i//10-((i//100)*10))+(i%10)+i
    else:
        return (i//10)+(i%10)+i
    
numlist=list(range(1,10000))
i=1
while True:
    try:
        div=divide(i)
        if div<10010:
            del numlist[numlist.index(div)]
            i=i+1
        else:
            break
    except:
        i=i+1
        pass
print("\n".join(map(str,numlist)))
