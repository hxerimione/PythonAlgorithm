import sys
from collections import deque
input = sys.stdin.readline
s = deque(list(input()[:-1]))

answer=[]
tmp = ""
num = 0
while s :
    i = s.popleft()
    if i=='-':
        num += int(tmp)
        answer.append(num)
        num=0
        tmp=""
    elif i=='+':
        num += int(tmp)
        tmp=""
    else:
        tmp+= i
num+=int(tmp)
answer.append(num)
ans=answer[0]
for a in answer[1:]:
    ans-=a
print(ans)