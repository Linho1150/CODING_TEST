mlist=[]
max=0
cnt=0
for num in range(0,9):
  tmp=int(input())
  if tmp>max:
    max=tmp
    cnt=num+1
print(max)
print(cnt)