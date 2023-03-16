import sys
input = sys.stdin.readline
from collections import deque
n,k =map(int,input().split())
arr = deque(list(map(int,input().split())))
robot = deque([0 for _ in range(n*2)])
count = 0
r =1

while True:
    count+=1
    #1.회전
    arr.rotate(1)
    robot.rotate(1)
    #2.로봇 위치 이동
    robot[n-1] =0
    for i in range(n-2,-1,-1):
        if robot[i]>0 and robot[i+1] ==0 and arr[i+1]>=1 :
            #내림
            if i+1 == n-1 :
                robot[i]=0
                arr[i+1]-=1
            else:
                robot[i+1] = i
                robot[i] = 0
                arr[i+1] -=1
    #3.새로 올리기
    if arr[0] >=1 and robot[0] ==0 :
        arr[0]= arr[0]-1
        robot[0]=r
        r+=1
    #4.
    if arr.count(0) >=k :
        print(count)
        break