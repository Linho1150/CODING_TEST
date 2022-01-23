cnt=int(input())
length=len(str(cnt))
count=99
tmp=0
if length==1 or length==2:
    print(cnt)
else:
    tmp=99
    while tmp<=cnt:
        if len(str(tmp))==3:
            if ((tmp//100)-((tmp//10)%10)) == (((tmp//10)%10)-(tmp%10)):
                count=count+1
        elif len(str(tmp))==4:
            if (tmp//1000)-((tmp//100)%10) == ((tmp//100)%10)-((tmp//10)%10) == ((tmp//10)%10)-(tmp%10):
                print((tmp//1000)-((tmp//100)%10),((tmp//100)%10)-((tmp//10)%10),((tmp//10)%10)-(tmp%10))
                count=count+1
        tmp=tmp+1
    print(count)