import sys
input = sys.stdin.readline
from collections import deque

one = deque(list(map(int,input().rstrip())))
two =deque(list(map(int,input().rstrip())))
three = deque(list(map(int,input().rstrip())))
four = deque(list(map(int,input().rstrip())))

q =deque()
n= int(input())
for _ in range(n):
    a,b = map(int,input().split())
    if a == 1 :
        q.append((1,b))
        if one[2] != two[6] :
            q.append((2,-b))
            if two[2] != three[6] :
                q.append((3,b))
                if three[2] != four[6]:
                    q.append((4,-b))
    elif a == 2:
        q.append((2,b))
        if one[2] != two[6] :
            q.append((1,-b))
        if two[2] != three[6] :
            q.append((3,-b))
            if three[2]!= four[6] :
                q.append((4,b))
    elif a == 3:
        q.append((3,b))
        if two[2]!=three[6] :
            q.append((2,-b))
            if one[2]!=two[6]:
                q.append((1,b))
        if three[2] != four[6] :
            q.append((4,-b))
    elif a == 4:
        q.append((4,b))
        if three[2] != four[6] :
            q.append((3,-b))
            if two[2] != three[6] :
                q.append((2,b))
                if one[2] != two[6]:
                    q.append((1,-b))
    
    while q:
        a,b = q.popleft()
        if a== 1:
            one.rotate(b)
        elif a==2:
            two.rotate(b)
        elif a==3:
            three.rotate(b)
        elif a==4:
            four.rotate(b)

answer =0
answer += one[0] + two[0]*2 + three[0]*4 + four[0]*8
print(answer)