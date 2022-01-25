target=int(input())
def fibo(n:int):
    if n-2<=0:
        return 1
    return fibo(n-1)+fibo(n-2)
if target==0:
    print(0)
else:
    print(fibo(target))