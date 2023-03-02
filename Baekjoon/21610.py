import sys
input =sys.stdin.readline
n,m = map(int,input().split())
bucket = []
for _ in range(n):
    bucket.append(list(map(int,input().split())))


dx,dy = [0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1]
wx,wy = [-1,1,1,-1],[-1,-1,1,1]
p = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for _ in range(m):
    visited = [[0]*n for _ in range(n)]
    a,b = map(int,input().split())
    #구름 이동
    for i in range(len(p)) :
        p[i][0] = (p[i][0] + dx[a]*(b%n))%n
        p[i][1] = (p[i][1] + dy[a]*(b%n))%n
        bucket[p[i][0]][p[i][1]] +=1
        visited[p[i][0]][p[i][1]] =1
          
    # 물복사 버그
    pp=[]
    for i in range(len(p)):
        tmp=0
        for k in range(4):
            nx = p[i][0] +wx[k]
            ny = p[i][1]+wy[k]
            if 0<=nx<n and 0<=ny<n and bucket[nx][ny] >0 :
                tmp+=1
        pp.append(tmp)
    for i in range(len(p)) :
        bucket[p[i][0]][p[i][1]] += pp[i]
    p=[]
    for i in range(n):
        for j in range(n):
            if bucket[i][j] >=2 and visited[i][j] ==0 :
                bucket[i][j] -=2
                p.append([i,j])
    
answer=0

for i in range(n):
    for j in range(n):
        answer+=bucket[i][j]

print(answer)