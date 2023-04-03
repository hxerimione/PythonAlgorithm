import sys
input = sys.stdin.readline
import heapq
n = int(input())
days=[]
stack=[]
for _ in range(n):
    m1,d1,m2,d2 = map(int,input().split())
    if m2<=2 and d2<=31:
        continue
    elif m1>=12 and d1>=1:
        continue
    else:
        days.append((100*m1 + d1,m2*100+d2))
days = sorted(days,key = lambda x : (x[0],x[1]))
stack=[(301)]

tmp=[]
while days:
    if stack[-1]<days[0][0] or stack[-1]>1200:
        break
    target=0
    for _ in range(len(days)) :
        if stack[-1] >=days[0][0]:
            if target<days[0][1]:
                target = days[0][1]
            days.remove(days[0])
        else:
            break
    stack.append(target)
if stack[-1]<1200:
    print(0)
else:
    print(len(stack)-1)