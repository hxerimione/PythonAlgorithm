import sys
input = sys.stdin.readline

from collections import deque
one = 0
zero=0
neg = []
pos = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m<0:
        neg.append(m)
    elif m>1 :
        pos.append(m)
    elif m ==1 :
        one +=1
    elif m==0 :
        zero+=1
neg.sort()
pos.sort()

answer=0
while neg :
    a = neg.pop(0)
    if neg :
        b = neg.pop(0)
        answer += a*b
    elif zero==0:
        answer += a
while pos :
    a = pos.pop()
    if pos:
        b = pos.pop()
        answer += a*b
    else:
        answer += a
print(answer+one)