def solution(a, b):
    answer=0
    for tmp in range(len(a)):
        answer=answer+(a[tmp]*b[tmp])
    return answer