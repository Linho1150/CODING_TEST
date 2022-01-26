A,B = map(int,input().split())
text = list(map(int,input().split()))
before=0

for x in range(A):
    for y in range(x+1,A):
        for z in range(y+1,A):
            value=text[x]+text[y]+text[z]
            if before<value<=B:
                before=value
print(before)