import sys
import heapq
from sys import maxsize
input = sys.stdin.readline
n,m = map(int,input().split())
graph= [[]for _ in range(n+1)]
visited = [maxsize]*(n+1)
start = int(input())
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0
    while pq :
        d,x = heapq.heappop(pq)
        if visited[x] < d:
            continue
        for nw,nx in graph[x]:
            nd = d+ nw
            if visited[nx] > nd :
                heapq.heappush(pq,(nd,nx))
                visited[nx] = nd

dijkstra(start)
for i in visited[1:]:
    if i == maxsize:
        print("INF")
    else:
        print(i)
