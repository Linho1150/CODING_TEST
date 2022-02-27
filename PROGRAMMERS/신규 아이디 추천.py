def solution(new_id):
    new_id=level1(new_id)
    new_id=level2(new_id)
    new_id=level3(new_id)
    new_id=level4(new_id)
    new_id=level5(new_id)
    new_id=level6(new_id)
    new_id=level7(new_id)
    return new_id

def level1(id):
    return id.lower()

def level2(id):
    result=""
    for tmp in id:
        if tmp.isalnum() or tmp=='-' or tmp=='_' or tmp=='.':
            result=result+tmp
    return result

def level3(id):
    while True:
        if '..' in id:
            id=id.replace('..','.')
        else:
            break
    return id

def level4(id):
    if id[0]=='.':
        id=id[1:]
    if len(id)>0:
        if id[-1]=='.':
            id=id[:-1]
    return id

def level5(id):
    if id=='':
        id='a'
    return id

def level6(id):
    if len(id)>=16:
        id=id[:15]
    if len(id)>0:
        if id[-1]=='.':
            id=id[:-1]
    return id

def level7(id):
    if len(id)<=2:
        while len(id)!=3:
            id=id+id[-1]
    return id