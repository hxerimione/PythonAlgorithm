import sys
import copy
input = sys.stdin.readline
dx,dy = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
arr=[]

max_score=0
answer =[]
for i in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())
    arr.append([[a,b-1],[c,d-1],[e,f-1],[g,h-1]])
def dfs(x,y,fish,board):
    global max_score
    fish += board[x][y][0]
    max_score = max(max_score,fish)
    board[x][y][0] =0
    for f in range(1, 17):
        fx,fy = -1,-1
        for xi in range(4):
            for yi in range(4):
                if board[xi][yi][0] ==f :
                    fx,fy = xi,yi
                    break
        if fx < 0 or fy < 0:
            continue
        b = board[fx][fy][1]
        for k in range(8):
            di = (b + k) % 8
            nx = fx + dx[di]
            ny = fy + dy[di]
            if 0 <= nx < 4 and 0 <= ny < 4 and not(nx ==x and ny==y):
                board[fx][fy][1] = di
                board[fx][fy],board[nx][ny] = board[nx][ny],board[fx][fy]
                break
    #상어 움직임
    fd = board[x][y][1]
    for i in range(1,4):
        sx = x + i*dx[fd]
        sy = y + i*dy[fd]
        if 0<=sx<4 and 0<=sy<4 and board[sx][sy][0]>0:
            dfs(sx,sy,fish,copy.deepcopy(board))


dfs(0,0,0,arr)
print(max_score)