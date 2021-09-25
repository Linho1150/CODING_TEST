import sys
input=sys.stdin.readline
num=list(map(int,input().split(' ')))

A=num[0]
B=num[1]
C=num[2]

if B>=C:
  print(-1)
else:
  print(int(A//(C-B)+1))