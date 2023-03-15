import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
answer=[N]
for i in range(N-2,-1,-1):
    answer = answer[:arr[i]] + [i+1] + answer[arr[i]:]
    
print(*answer)