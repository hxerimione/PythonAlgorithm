import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))
nums.insert(0,0)
location = [0 for _ in range(n+1)]
for i in range(1,n+1):
    location[nums[i]] = i
count=1
max_num =-1
dp = [1 for _ in range(n)]
dp.insert(0,0)
for i in range(n):
    if location[i]<location[i+1]:
        
        dp[i+1] = dp[i] +1
print(dp)     
print(n-max(dp))
