import sys
inputTxt=[]
while True:
    txt = sys.stdin.readline()
    if txt=="":
        break
    else:
        inputTxt.append(txt)

def check(text):
    tmp=[]
    for cnt in range(len(text)):
        sep=text[cnt]
        if sep=='(':
            tmp.append('(')
        elif sep==')':
            tmp.append(')')
        elif sep=='[':
            tmp.append('[')
        elif sep==']':
            tmp.append(']')
       
    tmp2=[]
    for txt in tmp:
        if txt=='(':
            tmp2.append('(')
        elif txt==')':
            if len(tmp2)==0:
                return False
            else:
                if tmp2[len(tmp2)-1]=='(':
                    tmp2=tmp2[:-1]
                else:
                    return False
        elif txt=='[':
            tmp2.append('[')
        elif txt==']':
            if len(tmp2)==0:
                return False
            else:
                if tmp2[len(tmp2)-1]=='[':
                    tmp2=tmp2[:-1]
                else:
                    return False
        else:
            return False
    if len(tmp2)==0:
        return True
    else:
        return False
    
inputTxt=inputTxt[:-1]
for tmp in inputTxt:
    tmp=tmp.replace('\n','')
    if check(tmp):
        print("yes")
    else:
        print("no")
        