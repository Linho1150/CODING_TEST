cnt=int(input())
count=1
top=1
bottom=0
if cnt==1:
    cnt=-1
    print('1/1')
    
for tmp in range(0,cnt+1):
    if count< cnt <= count+(tmp+2):
        if (tmp+2)%2==0:
            bottom=tmp+2
            top=1
            for tmp1 in range(cnt-count-1):
                top=top+1
                bottom=bottom-1
        else:
            top=tmp+2
            bottom=1
            for tmp1 in range(cnt-count-1):
                bottom=bottom+1
                top=top-1
        print(str(top)+'/'+str(bottom))
        break
    count=count+(tmp+2)