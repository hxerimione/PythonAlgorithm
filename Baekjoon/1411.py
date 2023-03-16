import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import Counter
n = int(input())

arr=[]
for i in range(n):
    arr.append(input()[:-1])

for i in range(n):
    string = arr[i]
    dic = defaultdict(int)
    tmp =1
    num=""
    for s in string :
        if dic[s] ==0 :
            dic[s] = tmp
            num+=str(tmp)
            tmp+=1
        else:
            num +=str(dic[s])
    arr[i] = num
answer=0
for k,v in Counter(arr).items():
    answer += v*(v-1)//2
print(answer)