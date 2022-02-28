def solution(answers):
    result=[0,0,0]
    answer=[]
    section1=[1,2,3,4,5]
    section2=[2,1,2,3,2,4,2,5]
    section3=[3,3,1,1,2,2,4,4,5,5]
    
    result[0]=step(answers,section1)
    result[1]=step(answers,section2)
    result[2]=step(answers,section3)

    value=max(result)
    for tmp in range(len(result)):
        if result[tmp]==value:
            answer.append(tmp+1)

    return answer

def step(target,section):
    cnt=0
    score=0
    for tmp in target:
        if tmp == section[cnt%len(section)]:
            score=score+1
        cnt=cnt+1
    return score