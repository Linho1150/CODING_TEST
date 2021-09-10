cnt=input()
mlist=map(int,input().split(' '))
max=-1000000
min=1000000
for tmp in mlist:
  if tmp>max:
    max=tmp
  if tmp<min:
    min=tmp

print(min,max)