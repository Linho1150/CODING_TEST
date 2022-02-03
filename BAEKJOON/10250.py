import sys
cnt=int(sys.stdin.readline())
for tmp in range(cnt):
    inputTxt=sys.stdin.readline()
    h,w,n=list(map(int,inputTxt.split()))
    nn=n%h
    hh=n//h+1
    if nn==0:
        nn=h
        hh=hh-1
    print(str(nn)+str(hh).zfill(2))