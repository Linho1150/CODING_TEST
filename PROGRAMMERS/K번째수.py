def solution(array, commands):
    result=[]
    for i,j,k in commands:
        result.append(do(array,i,j,k))
    return result

def do(target,i,j,k):
    result=step1(target,i,j)
    result=step2(result)
    result=step3(result,k)
    print(result)
    return result
    
def step1(target,i,j):
    return target[i-1:j]
    
def step2(target):
    return sorted(target)

def step3(target,k):
    return target[k-1]