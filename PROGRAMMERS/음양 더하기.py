def solution(absolutes, signs):
    result=0
    for tmp in range(len(signs)):
        if signs[tmp]==True:
            result=result+absolutes[tmp]
        else:
            result=result-absolutes[tmp]
    return result