cnt=int(input())
wordList=[]
for cntTmp in range(cnt):
    cntWord,tmpWord=input().split()
    cntWord=int(cntWord)
    tmpWord=list(tmpWord)
    for letter in tmpWord:
        print(letter*cntWord,end="")
    print()
    