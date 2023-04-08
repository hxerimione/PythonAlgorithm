root = []
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def snail(n):
    x = (n - 1) // 2
    y = (n - 1) // 2
    d = 0
    root.append([x, y,0])
    for i in range(1, n):
        for _ in range(2):
            for _ in range(i):
                nx = x + dx[d]
                ny = y + dy[d]
                x, y = nx, ny
                root.append([x,y,d])
            d=(d+1)%4
            root[-1][2]= d
    for _ in range(n-1):
        nx = x + dx[d]
        ny = y + dy[d]
        x,y = nx,ny
        root.append([x,y,d])

    d = (d+2)%4
    root[-1][2]=d

    for i in range(n-1):
        nx = x+dx[d]
        ny = y+dy[d]
        x,y = nx,ny
        root.append([x,y,d])
    d = (d+3)%4
    root[-1][2] = d
    for i in range(n-1,0,-1):
        for _ in range(2):
            for _ in range(i):
                nx = x + dx[d]
                ny = y + dy[d]
                x, y = nx, ny
                root.append([x,y,d])
            d=(d+3)%4
            root[-1][2]= d
    root.pop()



from collections import deque
n,m,h,k = map(int,input().split())
snail(n)
tree = [[0 for _ in range(n)]for _ in range(n)]

location=deque()
direct=deque()
for _ in range(m):
    a,b, d = map(int,input().split())
    location.append([a-1,b-1])
    direct.append(d)
    #graph[a-1][b-1].append(d)
for _ in range(h):
    a,b = map(int,input().split())
    tree[a-1][b-1] = 1
    #graph[a][b].append(4)
answer=0
def run_move(sx,sy):
    for i in range(len(location)):
        a,b= location[i]
        d = direct[i]
        if abs(a-sx) + abs(b-sy)<=3 :
            nx = a+dx[d]
            ny = b+dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not (nx == sx and ny == sy):
                    location[i] = [nx,ny]
            else:
                nd = (d + 2) % 4
                nx = a + dx[nd]
                ny = b + dy[nd]
                if not (nx == sx and ny == sy):
                    location[i] = [nx,ny]
                    direct[i] = nd

def catch(x,y):
    tmp=0

    for i in range(len(location)):
        a,b = location.popleft()
        dd = direct.popleft()
        if a==x and b==y :
           tmp +=1
        else:
            location.append([a,b])
            direct.append(dd)
    return tmp
def move(sx,sy,sd):
    cnt=0
    if tree[sx][sy] ==0 and [sx,sy] in location :
        cnt += catch(sx,sy)
    for _ in range(2):
        sx = sx + dx[sd]
        sy = sy + dy[sd]
        if 0<=sx<n and 0<=sy<n :
            if tree[sx][sy] ==1:
                continue
            elif [sx,sy] in location :
                cnt += catch(sx,sy)
    return cnt

for t in range(1,k+1):
    g = 2*(n**2)-2
    i = t%g

    sx,sy,sd = root[i-1]
    run_move(sx,sy)
    sx,sy,sd = root[i]
    cnt = move(sx,sy,sd)
    answer += t*cnt
print(answer)


