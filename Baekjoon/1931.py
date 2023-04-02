import sys
input = sys.stdin.readline
import heapq

que= []
stack=[0]
n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    que.append((s,e))
que = sorted(que,key = lambda x :(x[1],x[0]))
for s,e in que :
    if stack[-1] <= s:
        stack.append(e)
print(len(stack)-1)
