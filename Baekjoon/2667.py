import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
dx,dy = [-1,1,0,0],[0,0,-1,1]
visited = [[0 for _ in range(n)] for _ in range(n)]
que = deque()
def bfs(i,j):
    que.append((i,j))
    count=0
    while que:
        count+=1
        x,y = que.pop()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny] ==1 :
                visited[nx][ny] = count
                que.append((nx,ny))
    return count
graph=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
answer=[]

for i in range(n):
    for j in range(n):
        if visited[i][j] ==0 and graph[i][j] == 1:
            visited[i][j] = 1
            answer.append(bfs(i,j))
            
print(len(answer))
answer.sort()
for a in answer:
    print(a)