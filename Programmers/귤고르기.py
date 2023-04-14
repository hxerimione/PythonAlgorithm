from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    d = defaultdict(int)
    for t in tangerine:
        d[t]+=1
    arr=[]
    for key,v in d.items():
        arr.append((key,v))
    arr = sorted(arr,key = lambda x: -x[1])
    tmp=0
    for t,n in arr :
        answer +=1
        tmp += n
        if tmp >=k:
            break
    return answer