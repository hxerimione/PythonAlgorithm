import sys
input = sys.stdin.readline

n= int(input())
dp=[0 for _ in range(1000001)]
dp[1]=1
dp[2]=2
dp[3]=4
arr=[]
for _ in range(n):
    arr.append(int(input()))
for i in range(4,max(arr)+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009
for a in arr :
    print(dp[a])