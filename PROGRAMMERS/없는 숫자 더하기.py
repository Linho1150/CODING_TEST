def solution(numbers):
    numList=[0,1,2,3,4,5,6,7,8,9]
    for tmp in numbers:
        numList[tmp]=0
    return sum(numList)