import sys
input =sys.stdin.readline

n = int(input())
times = [[0,0]]
for _ in range(n):
    a,b = map(int,input().split())
    times.append([a,b])
dp=[0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i] = max(dp[i],dp[i-1])
    if i+times[i][0]-1<=n:
        dp[i+times[i][0]-1] =max(dp[i+times[i][0]-1],dp[i-1]+times[i][1])
    
print(dp[-1])