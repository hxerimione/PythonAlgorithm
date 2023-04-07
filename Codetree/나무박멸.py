import math

n,m,k,c = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,0,1,0],[0,-1,0,1]
dsx,dsy = [-1,-1,1,1],[-1,1,-1,1]
herbicide = [[0 for _ in range(n)] for _ in range(n)]
answer=0
def growth():
    for i in range(n):
        for j in range(n):
            if graph[i][j] >0:
                cnt=0
                for t in range(4):
                    nx = i +dx[t]
                    ny = j +dy[t]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                        cnt+=1
                graph[i][j] += cnt
def breeding(visit):
    tmp=[]
    plus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                cnt=0

                for t in range(4):
                    nx = i+dx[t]
                    ny = j+dy[t]
                    if 0<=nx<n and 0<=ny<n and visit[nx][ny] and herbicide[nx][ny]==0:
                        tmp.append((nx,ny))
                        cnt+=1
                while tmp :
                    a,b = tmp.pop()
                    plus.append((a,b,math.floor(graph[i][j]/cnt)))
    while plus:
        a,b,f = plus.pop()
        graph[a][b]+=f

def killcount():
    q=[]
    max_size=0
    a,b = -1,-1
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            killed = [[False for _ in range(n)] for _ in range(n)]

            cnt=graph[i][j]
            if graph[i][j]>0:
                for t in range(4):
                    nx = i+dsx[t]
                    ny = j+dsy[t]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0 and not killed[nx][ny]:
                        q.append((1,nx,ny,t))
                        cnt+=graph[nx][ny]
                        killed[nx][ny]=True
                while q :
                    d,x,y,drt = q.pop()
                    if d== k:
                        continue
                    nx = x+dsx[drt]
                    ny = y+dsy[drt]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0 and not killed[nx][ny]:
                        q.append((d + 1, nx, ny, drt))
                        cnt += graph[nx][ny]
                        killed[nx][ny] = True

                if cnt >= max_size:
                    max_size = cnt
                    a,b = i,j
    return a,b

def kill(x,y):
    global answer
    q = []
    cnt=graph[x][y]
    herbicide[x][y]=c+1
    for t in range(4):
        nx = x + dsx[t]
        ny = y + dsy[t]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny]==-1:
                continue
            herbicide[nx][ny] = c+1
            if graph[nx][ny] > 0 :
                q.append((1, nx, ny, t))
                cnt += graph[nx][ny]
    while q:
        d, x, y, drt = q.pop()
        if d == k:
            continue
        nx = x + dsx[drt]
        ny = y + dsy[drt]
        if 0 <= nx < n and 0 <= ny < n :
            if graph[nx][ny]==-1:
                continue
            herbicide[nx][ny] = c+1
            if graph[nx][ny] > 0 :
                q.append((d + 1, nx, ny, drt))
                cnt += graph[nx][ny]
    answer +=cnt
def minus():
    for i in range(n):
        for j in range(n):
            if herbicide[i][j]>1:
                herbicide[i][j]-=1
                graph[i][j]=-2
            elif herbicide[i][j]==1:
                herbicide[i][j]-=1
                graph[i][j]=0

for _ in range(m):
    #1.성장
    growth()
    #2.번식
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] ==0 and herbicide[i][j] ==0 :
                visit[i][j]=True
    breeding(visit)
    #3.제일 박멸 가능 수 큰 나무 조사
    x,y = killcount()
    #4.박멸
    if x>-1 and y>-1:
        kill(x,y)
    #5.제초제 줄이기
    minus()
print(answer)