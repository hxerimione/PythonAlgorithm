import sys
from collections import deque
input = sys.stdin.readline
nn, Q = map(int, input().split())
N = 2 ** nn
arr = []
visited = [[0 for _ in range(N)] for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(N):
    arr.append(list(map(int, input().split())))
List = list(map(int, input().split()))
lump =[0]
def rotate(x1,y1,L):
    new = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(L):
        for j in range(L):
            new[j][L-1-i] = arr[i+x1][j+y1]

    for i in range(L):
        for j in range(L):
            arr[i + x1][j + y1] = new[i][j]


def ice():
    q = deque()
    for i in range(N):
        for j in range(N):
            count = 0
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
                    count += 1
            if count < 3:
                q.append((i, j))
    while q:
        a, b = q.popleft()
        if arr[a][b]>0:
            arr[a][b] -= 1

def bfs(x,y):
    q=deque()
    q.append((x,y))
    count=0
    while q:
        a,b = q.popleft()
        count+=1
        for k in range(4):
            nx = a+dx[k]
            ny = b+dy[k]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]>0 and visited[nx][ny]==0:
                visited[nx][ny] =1
                q.append((nx,ny))
    lump.append(count)

for l in List:
    L = 2 ** l
    if l>0:
        for i in range(0, N, L):
            for j in range(0, N, L):
                rotate(i, j,L)

    ice()
hap=0
for i in range(N):
    for j in range(N):
        hap += arr[i][j]
        if arr[i][j]>0 and visited[i][j]==0 :
            visited[i][j]=1
            bfs(i,j)

print(hap)
print(max(lump))