import sys
input = sys.stdin.readline

t,w =map(int,input().split())
arr=[0]
dp=[[0 for _ in range(w+1)]for _ in range(t+1)]

for _ in range(t):
    arr.append(int(input()))
for i in range(t+1):
    for j in range(w+1):
        if j==0 :
            if arr[i] ==1 :
                dp[i][j] = dp[i-1][j] +1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if arr[i] == 2 and j%2==1:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1
            elif arr[i] ==1 and j%2==0 :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])

print(dp)
print(max(dp[t]))