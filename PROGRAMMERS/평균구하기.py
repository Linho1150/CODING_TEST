def solution(arr):
    sum=0
    for tmp in arr:
        sum=sum+tmp
    answer = sum/len(arr)
    return answer