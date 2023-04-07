n,m,k =map(int,input().split())
graph = [[[]for _ in range(n)]for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j]>0:
            graph[i][j].append(arr[j])
direct=[]
location=[[-1 for _ in range(n)]for _ in range(n)]
point=[0 for _ in range(m)]
gun=[0 for _ in range(m)]
power=[]
dx,dy=[-1,0,1,0],[0,1,0,-1]
for i in range(m):
    x,y,d,p = map(int,input().split())
    location[x-1][y-1] = i
    direct.append(d)
    power.append(p)
def getgun(player,x,y):
    if len(graph[x][y])>0:
        tmp = max(graph[x][y])
        if tmp > gun[player]:
            graph[x][y].remove(tmp)
            if gun[player]>0:
                graph[x][y].append(gun[player])
            gun[player] = tmp

def win(winner,winpoint):
    point[winner]+=winpoint
def lose(loser,x,y):
    if gun[loser]>0:
        graph[x][y].append(gun[loser])
        gun[loser]=0
    for k in range(4):
        nx = x+dx[(direct[loser]+k)%4]
        ny = y+dy[(direct[loser]+k)%4]
        if 0<=nx<n and 0<=ny<n and location[nx][ny]==-1:
            direct[loser] = (direct[loser]+k)%4
            location[nx][ny] = loser
            getgun(loser,nx,ny)
            break
for _ in range(k):
    for i in range(m):
        x,y =0,0
        #1.가까운 곳으로 이동
        for a in range(n):
            for b in range(n):
                if location[a][b] == i:
                    x,y = a,b
                    break
        nx = x+dx[direct[i]]
        ny = y+dy[direct[i]]
        if not(0<=nx<n and 0<=ny<n):
            direct[i] = (direct[i]+2)%4
            nx = x+dx[direct[i]]
            ny = y+dy[direct[i]]
        location[x][y]=-1
        #2.이동한 칸에 플레이어 없고 총(들)이 있다면
        winner=-1
        loser=-1
        winpoint= 0
        if location[nx][ny]==-1:
            getgun(i,nx,ny)
            location[nx][ny] = i
        #3.이동한 칸에 플레이어가 있다면
        else:
            p1 = i
            p2 = location[nx][ny]
            power1 = power[p1]+gun[p1]
            power2 = power[p2]+gun[p2]
            winpoint=abs(power1-power2)
            if power1 >power2:
                #winner : p1
                winner = p1
                loser = p2
            elif power1 <power2:
                #winner : p2
                winner = p2
                loser = p1
            else:
                if power[p1]>power[p2]:
                    #winner : p1
                    winner = p1
                    loser = p2
                else:
                    #winner : p2
                    winner = p2
                    loser = p1
            win(winner,winpoint)
            lose(loser,nx,ny)
            getgun(winner,nx,ny)
            location[nx][ny] = winner
print(*point)
