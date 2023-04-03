import sys
input =sys.stdin.readline

n = int(input())
times = [[0,0]]
for _ in range(n):
    a,b = map(int,input().split())
    times.append([a,b])
dp=[0 for _ in range(n+1)]
for i in range(n):
    print(dp)
    if i+times[i][0]-1<=n:
        dp[i+times[i][0]-1] = dp[i+times[i][0]-2] + max(dp[i+times[i][0]-1],dp[i]+times[i][1])
print(dp)