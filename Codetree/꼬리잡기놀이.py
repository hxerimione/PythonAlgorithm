n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
from collections import deque
answer =0
def move(x,y):
    q = deque()
    flag = False
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 4:
                graph[nx][ny] = 1
                graph[x][y] = 2
                visit[nx][ny]=True
                break
            elif graph[nx][ny] == 3:
                visit[nx][ny]=True
                flag = True
                for d in range(4):
                    sx = nx + dx[d]
                    sy = ny + dy[d]
                    if 0 <= sx < n and 0 <= sy < n and graph[sx][sy] == 2:
                        graph[sx][sy] = 3
                        graph[nx][ny] = 1
                        graph[x][y] = 2

    if flag:
        return
    q.append((x, y))
    visit[x][y]=True
    while q:
        i, j = q.pop()
        for t in range(4):
            nx = i + dx[t]
            ny = j + dy[t]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] == 2:
                    graph[i][j] = 2
                    q.append((nx, ny))
                    visit[nx][ny] = True
                elif graph[nx][ny] == 3:
                    graph[nx][ny] = 4
                    graph[i][j] = 3

def change(x,y):
    global answer
    visit = [[False for _ in range(n)]for _ in range(n)]
    q = deque()
    x1,y1,x3,y3 = -1,-1,-1,-1
    if graph[x][y]==1 :
        answer += 1
        visit[x][y]=True
        q.append((1,x,y))
        while q :
            d,i,j = q.pop()
            for t in range(4):
                nx = i+dx[t]
                ny = j+dy[t]
                if 0<=nx<n and 0<=ny<n :
                    if graph[nx][ny]==2 :
                        if not visit[nx][ny]:
                            visit[nx][ny] = True
                            q.append((d+1,nx,ny))
                    elif graph[nx][ny]==3 and not visit[nx][ny] :
                        graph[x][y],graph[nx][ny] = graph[nx][ny],graph[x][y]
    elif graph[x][y]==3 :
        visit[x][y] =True
        q.append((1,x,y))
        while q :
            d,i,j = q.pop()
            for t in range(4):
                nx = i+dx[t]
                ny = j+dy[t]
                if 0<=nx<n and 0<=ny<n :
                    if graph[nx][ny]==2 :
                        if not visit[nx][ny]:
                            visit[nx][ny] = True
                            q.append((d+1,nx,ny))
                    elif graph[nx][ny] ==1 and not visit[nx][ny] and d+1>2:
                        graph[x][y],graph[nx][ny] = graph[nx][ny],graph[x][y]
                        answer += (d+1)**2
    else:
        #2->1, 2->3
        visit[x][y] = True
        q.append((1,x,y))
        while q:
            d,i,j = q.popleft()
            for t in range(4):
                nx = i+dx[t]
                ny = j+dy[t]
                if 0<=nx<n and 0<=ny<n :
                    if graph[nx][ny] ==2 :
                        if not visit[nx][ny]:
                            visit[nx][ny] = True
                            q.append((d+1,nx,ny))
                    elif graph[nx][ny]==1:
                        answer += (d+1)**2
                        x1,y1 = nx,ny
                    elif graph[nx][ny]==3:
                        visit[nx][ny] =True
                        x3,y3 = nx,ny
        graph[x1][y1],graph[x3][y3] = graph[x3][y3],graph[x1][y1]


def ball(round):
    direct = ((round-1)//n)%4
    num = (round-1)%n
    a,b=-1,-1
    if direct ==0:
        for j in range(n):
            if 1<=graph[num][j]<=3:
                a,b = num,j
                break
    elif direct==1:
        for i in range(n-1,-1,-1):
            if 1<=graph[i][num]<=3:
                a,b = i,num
                break
    elif direct==2:
        for j in range(n-1,-1,-1):
            if 1<=graph[n-1-num][j]<=3:
                a,b = n-1-num,j
                break
    elif direct==3:
        for i in range(n):
            if 1<=graph[i][n-1-num]<=3:
                a,b = i,n-1-num
                break
    if a>-1 and b>-1:
        change(a,b)

for round in range(1,k+1):
    visit = [[False for _ in range(n)]for _ in range(n)]
    # 1. move
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visit[i][j]:
                move(i, j)

    #2. 공던지기
    ball(round)
print(answer)