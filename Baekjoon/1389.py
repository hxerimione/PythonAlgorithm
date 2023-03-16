import sys
input = sys.stdin.readline
from collections import deque
def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue :
        target = queue.popleft()
        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target]+1
                queue.append(i)
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
res=[]

for i in range(1,N+1):
    visited = [0] *(N+1)
    bfs(i)
    res.append(sum(visited))
print(res.index(min(res))+1)