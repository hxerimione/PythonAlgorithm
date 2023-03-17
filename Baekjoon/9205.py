import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
con = []
for _ in range(n):
    flag = True
    con=[]
    m = int(input())
    #집
    s1,s2 = map(int,input().split())
    for i in range(m):
        con.append(list(map(int,input().split())))
    f1,f2 = map(int,input().split())
    q = deque()
    q.append((s1,s2))
    visited = [0 for _ in range(m)]
    while q :
        x,y = q.pop()
        if abs(f1-x)+abs(f2-y) <=1000 :
            print("happy")
            flag = False
            break
        for i in range(m):
            if not visited[i] and abs(con[i][0]-x)+abs(con[i][1]-y) <=1000:
                visited[i] =1
                q.append((con[i][0],con[i][1]))
    if flag :
        print("sad")
                
    
        