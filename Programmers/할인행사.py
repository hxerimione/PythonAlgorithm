from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    d = defaultdict(int)
    for w,n in zip(want,number):
        d[w]=n
    
    for i in range(10):
        if discount[i] in d:
            d[discount[i]]-=1
    flag = True
    for k,v in d.items():
        if v!=0:
            flag = False
            break
    
    if flag :
        answer+=1
    cur=0
    for i in range(len(discount)-10):
        if discount[cur] in d:
            d[discount[cur]]+=1
        cur+=1
        if discount[cur+9] in d :
            d[discount[cur+9]]-=1
        flag = True
        for k,v in d.items():
            if v!=0:
                flag = False
                break
        if flag:
            answer+=1
    return answer