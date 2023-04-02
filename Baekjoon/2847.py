import sys
input = sys.stdin.readline

n =int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
max=20001
answer=0
for i in range(len(arr)-1,-1,-1):
    if max <= arr[i] :
        answer += arr[i]-max+1
        arr[i] = max-1

    max = arr[i]

print(answer)