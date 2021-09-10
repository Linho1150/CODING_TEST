mlist=[]
cnt=[0,0,0,0,0,0,0,0,0,0]
num=1
for tmp in range(0,3):
  num=num*int(input())

for tmp in range(len(str(num))):
  number=int(str(num)[tmp])
  cnt[number]=cnt[number]+1

for tmp in range(len(cnt)):
  print(cnt[tmp])