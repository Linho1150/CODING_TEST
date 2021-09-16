numStr=input()
numStr=numStr.strip()
numStr=numStr.split(' ')
if len(numStr)==1 and numStr[0]=='':
  print(0)
else:
  print(len(numStr))