#import sys
#input = sys.stdin.readline
from collections import deque

dx,dy = [-1,0,1,0],[0,-1,0,1]
answer=0
def bfs(graph,visit,x,y,blocks,br):
    global color_x,color_y

    color = graph[x][y]
    q=deque()
    visit[x][y] =1
    q.append((x,y))
    tmp=[]
    tmp.append([x,y])
    rbw=0
    while q:
        i,j = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if graph[nx][ny] ==color and visit[nx][ny] ==0:
                    visit[nx][ny] =1
                    q.append((nx,ny))
                    tmp.append([nx,ny])
                elif graph[nx][ny]==0 and [nx,ny] not in tmp:
                    rbw+=1
                    q.append((nx,ny))
                    tmp.append([nx,ny])
    if len(tmp)>=2 and len(tmp)>len(blocks):
        blocks = tmp[:]
        br = rbw
        color_x = x
        color_y = y
    elif len(tmp)==len(blocks):
        if rbw>br:
            br = rbw
            blocks=tmp[:]
            color_x = x
            color_y = y
        elif rbw==br:
            if color_x<x:
                br = rbw
                blocks = tmp[:]
                color_x = x
                color_y = y
            elif color_x==x and color_y<y:
                br = rbw
                blocks = tmp[:]
                color_x = x
                color_y = y
    return visit,blocks,br
def big(graph):
    global color_x,color_y
    color_x,color_y = len(graph),len(graph)
    visit = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    blocks=[]
    br=0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]>=1 and visit[i][j]==0:
                visit,blocks,br= bfs(graph,visit,i,j,blocks,br)
    return blocks
def delete(graph,blocks):
    global answer
    answer += len(blocks)**2
    for x,y in blocks :
        graph[x][y] = -2
    return graph

def gravity(graph):
    for j in range(len(graph)):
        que=deque()
        tmp=deque()
        stack=[]
        cnt=0
        for i in range(len(graph)):
            que.append(graph[i][j])
        while que :
            a = que.popleft()
            if a>=0:
                tmp.append(a)
            elif a==-1:
                for _ in range(cnt):
                    stack.append(-2)
                cnt=0
                while tmp:
                    stack.append(tmp.popleft())
                stack.append(-1)
            elif a==-2:
                cnt+=1
        for _ in range(cnt):
            stack.append(-2)
        stack+=tmp
        for i in range(len(graph)):
            graph[i][j] = stack[i]
    return graph
def rotate(graph):
    tmp = [[0 for _ in range(len(graph))]for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            tmp[len(graph)-j-1][i] = graph[i][j]
    return tmp
N,M = map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(N)]

while True :
    tmp=0
    blocks=[]
    #1.제일 큰 블록그룹 구하기
    blocks=big(graph)
    if len(blocks)==0:
        break
    #2.제거하기
    graph = delete(graph,blocks)
    #3.중력작용
    graph = gravity(graph)
    #4.90도 회전
    graph = rotate(graph)
    #5.중력작용
    graph = gravity(graph)

print(answer)
