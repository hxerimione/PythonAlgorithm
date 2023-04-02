import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    answer=0
    m= int(input())
    nums = list(map(int,input().split()))
    M = 0
    for i in range(m-1,-1,-1) :
        if nums[i]>M:
            M = nums[i]
        else:
            answer += M-nums[i]
    print(answer)
    