import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
q = deque()
dist = []
visited=[-1 for _ in range(n+1)]
visited[x] = 0 
def bfs(x):
    d=0
    q.append(x)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == -1 :
                visited[i] = visited[x]+1
                q.append(i)
        d+=1
bfs(x)
if k in visited :
    for i in range(1,n+1):
        if visited[i] == k :
            print(i)
else:
    print(-1)

