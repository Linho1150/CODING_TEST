input1,input2=input().split()
input1=int("".join(list(reversed(input1))))
input2=int("".join(list(reversed(input2))))
if input1>input2:
    print(input1)
else:
    print(input2)