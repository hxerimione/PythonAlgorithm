import sys
input = sys.stdin.readline
import math
n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
global answer
dx,dy = [0,1,0,-1],[-1,0,1,0]

def wind(nx,ny,p,sand,tmp,out):
    if 0<=nx<n and 0<=ny<n:
        arr[nx][ny] += math.floor(sand*(p))
        tmp += math.floor(sand*(p))
    else:
        out += math.floor(sand*(p))
    return tmp,out
def tornado(x,y,d):
    global answer
    sand = arr[x][y]
    tmp=0
    out=0
    #7%-1
    nx = dx[d-1]+x
    ny = dy[d-1]+y
    tmp,out = wind(nx,ny,0.07,sand,tmp,out)
    #7%-2
    nx = dx[(d+1)%4]+x
    ny = dy[(d+1)%4]+y
    tmp,out = wind(nx,ny,0.07,sand,tmp,out)
    #2%-1
    nx = 2*dx[d-1]+x
    ny = 2*dy[d-1]+y
    tmp,out = wind(nx,ny,0.02,sand,tmp,out)
    #2%-2
    nx = 2*dx[(d+1)%4]+x
    ny = 2*dy[(d+1)%4]+y
    tmp,out = wind(nx,ny,0.02,sand,tmp,out)
    #5%-1
    nx = 2*dx[d] + x
    ny = 2*dy[d] + y
    tmp,out = wind(nx, ny, 0.05, sand, tmp, out)
    #10% -1
    nx = x+dx[d]+dx[(d+1)%4]
    ny = y+dy[d]+dy[(d+1)%4]
    tmp,out = wind(nx,ny,0.1,sand,tmp,out)
    #10%-2
    nx = x+dx[d]+dx[d-1]
    ny = y+dy[d]+dy[d-1]
    tmp,out = wind(nx,ny,0.1,sand,tmp,out)
    #1%-1
    nx = x+dx[d-2]+dx[d-1]
    ny = y+dy[d-2]+dy[d-1]
    tmp,out = wind(nx,ny,0.01,sand,tmp,out)
    #1%-2
    nx = x+dx[d-2]+dx[(d+1)%4]
    ny = y+dy[d-2]+dy[(d+1)%4]
    tmp,out = wind(nx,ny,0.01,sand,tmp,out)
    #alpha
    nx = x+dx[d]
    ny = y+dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand-tmp-out
    else:
        out += sand-tmp-out
    answer += out
def main():
    global answer
    x = round((n-1)/2)
    y = round((n-1)/2)
    d=0
    count=1
    answer=0
    while (x!=0 or y!=0):
        for _ in range(2):
            for _ in range(count):
                x = dx[d] + x
                y = dy[d] + y
                tornado(x,y,d)
                arr[x][y] =0
                if x==0 and y==0:
                    return
            d = (d+1)%4
        count+=1
main()
print(answer)