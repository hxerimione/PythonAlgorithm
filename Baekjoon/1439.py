import sys
input = sys.stdin.readline
s = input()[:-1]
cur=s[0]
answer=1

for i in s[1:]:
    if cur == i:
        continue
    else:
        cur = i
        answer+=1
print(answer//2)