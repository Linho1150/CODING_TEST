mlist=[]
for tmp in range(10):
  num=str(int(input())%42)
  if num not in mlist:
    mlist.append(num)
print(len(mlist))