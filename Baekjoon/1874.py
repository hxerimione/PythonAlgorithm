import sys

input = sys.stdin.readline
n = int(input())
answer=[]
stack=[]
flag = 0
cur=1
for _ in range(n):
    num = int(input())
    while cur<=num :
        stack.append(cur)
        answer.append("+")
        cur+=1
    if stack[-1] == num :
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if not flag :
    for i in answer:
        print(i)



