import sys
input =sys.stdin.readline
import copy

M,S = map(int,input().split())
graph = [[[]for _ in range(4)]for _ in range(4)]
dx,dy = [0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]
dsx,dsy = [-1,0,1,0],[0,-1,0,1]
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a-1][b-1].append(c-1)
s1,s2 = map(int,input().split())
shark =s1-1,s2-1
smell = [[0 for _ in range(4)] for _ in range(4)]

eat=[]
def move_fish():
    res = [[[]for _ in range(4)]for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while graph[i][j]:
                d = graph[i][j].pop()
                for k in range(8):
                    nd = (d+8-k)%8
                    nx = i+dx[nd]
                    ny = j+dy[nd]
                    if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and not (nx == shark[0] and ny == shark[1]):
                        res[nx][ny].append(nd)
                        break
                else:
                    res[i][j].append(d)
    return res
def dfs(sx,sy,visit,dep,cnt):
    global max_eat,eat,shark
    if dep==3:
        if max_eat<cnt:
            eat = visit[:]
            shark=[sx,sy]
            max_eat = cnt
        return
    for i in range(4):
        nx = sx+dsx[i]
        ny = sy+dsy[i]
        if 0<=nx<4 and 0<=ny<4:
            if [nx,ny] not in visit:
                visit.append([nx,ny])
                dfs(nx,ny,visit,dep+1,cnt+len(graph[nx][ny]))
                visit.pop()
            else:
                dfs(nx,ny,visit,dep+1,cnt)

for _ in range(S):
    #1.물고기 복제
    copy_fish =copy.deepcopy(graph)
    fish=[]
    #2.이동
    graph = move_fish()
    #3.상어 이동
    max_eat=-1
    visit=[]
    dfs(shark[0],shark[1],visit,0,0)

    for x,y in eat:
        if len(graph[x][y])>0:
            graph[x][y]=[]
            smell[x][y]=3
    #4.냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[i][j] >0:
                smell[i][j]-=1
    #5.복제마법
    for i in range(4):
        for j in range(4):
            graph[i][j]+=copy_fish[i][j]
    #answer
    answer=0
    for i in range(4):
        for j in range(4):
            answer += len(graph[i][j])

print(answer)