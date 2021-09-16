num = int(input())
mlist = map(int, input().split())
mlist = list(mlist)
nlist=[]
max = max(mlist)
for tmp1 in range(num):
  nlist.append(mlist[tmp1]/max*100)

total=0
for tmp2 in range(num):
  total=total+nlist[tmp2]
print((total/num))