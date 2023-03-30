import sys
import heapq
input = sys.stdin.readline

n= int(input())
q =[]
answer = []
for _ in range(n):
    l,r = map(int,input().split())
    heapq.heappush(q,(l,r))

answer=0
start,end = heapq.heappop(q)
while q:
    l,r = heapq.heappop(q)
    if end >= l and end <r:
        end = r
    elif end>=l and end >= r:
        continue
    else:
        answer += end-start
        start,end = l,r
answer += end-start
print(answer)
