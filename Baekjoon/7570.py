import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))
nums = [0] + nums
dp= [0 for _ in range(n+1)]

for i in range(1,n+1):
    idx = nums[i]
    dp[i] = dp[nums.index(nums[i]-1)] +1
    

print(n-max(dp))
